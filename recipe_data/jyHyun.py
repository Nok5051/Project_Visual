import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import re
from pandas import DataFrame

import json

service = Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

categories = [53, 54, 55, 56, 61, 65]
menu_ul = list()
menu_list = list()
servings = list()
ingredients = list()
units = list()
recipes = list()

# 음식 카테고리 > 메뉴 리스트
for category in categories:
    target_url = f'https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4={category}&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
    resp = requests.get(target_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    menu_ul.extend(soup.select('ul[class="tag_cont"] > li > a'))

for menu in menu_ul:
    menu_list.append(menu.text)


# print(menu_list) - 파스타, 라면 , ... 총 176개



# 메뉴 정확순 정렬
# test_menu = menu_list[21:22]
# for menu in test_menu:
for menu in menu_list:
    url = f'https://www.10000recipe.com/recipe/list.html?q={menu}&query=&cat1=&cat2=&cat3=&cat4=&fct=&order=accuracy&lastcate=order&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
    driver.get(url)
    # 3초 이하일 경우 크롤링을 제대로 수행하지 못함
    sleep(3)

    # 첫 번째 레시피 - 재료, 단위, 레시피 크롤링
    recipe_xpath = '//*[@id="contents_area_full"]/ul/ul/li[1]/div[1]/a'
    recipe = driver.find_element(By.XPATH, recipe_xpath)

    recipe_url = recipe.get_attribute('href')
    print(menu, recipe_url)
    resp = requests.get(recipe_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    try:
        serving = soup.select_one('span[class=view2_summary_info1]')
        servings.append(serving.text)

        recipe = soup.select('div[class="media-body"]')
        # 전처리
        recipe_n = list()
        for i in recipe:
            if i.has_attr('id'):
                recipe_n.extend(i)
        recipes.append(recipe_n)

        # 레시피 내부 태그 제거 작업
        for j in range(len(recipes)):
            for n in range(len(recipes[j])):
                if type(recipes[j][n]) == bs4.element.Tag:
                    recipes[j][n] = recipes[j][n].text
                else:
                    pass

        unit = soup.select('span[class="ingre_unit"]')
        # 전처리
        units_n = list()
        for i in unit:
            units_n.append(i.text)
        units.append(units_n)

        ingredient = soup.select('#divConfirmedMaterialArea > ul > a > li')
        #  전처리
        igd_n = list()
        for i in ingredient:
            i.find("img").decompose()
            i.find("a").decompose()
            i.find("span").decompose()
            i = i.text.replace("\n\n\n", "").rstrip()
            igd_n.append(i)
        ingredients.append(igd_n)

    except:
        servings.append("")
        recipes.append("")
        units.append("")
        ingredients.append("")


# print(test_menu)
# print(servings)
# print(recipes)

# print(ingredients)
# print(units)



# 레시피 데이터프레임 - 메뉴명, 인분, 레시피
# data = {'RECIPE_NM': test_menu, 'QNT': servings, 'RECIPE': recipes}
data = {'RECIPE_NM': menu_list, 'QNT': servings, 'RECIPE': recipes}
df = DataFrame(data)
with open('./recipe_table.json', 'w', encoding='utf-8') as file:
    df.to_json(file, force_ascii=False)

# 재료 데이터프레임 - 메뉴명, 재료, 용량
# data = {'RECIPE_NM': test_menu, 'INGREDIENTS': ingredients, 'UNITS': units}
data = {'RECIPE_NM': menu_list, 'INGREDIENTS': ingredients, 'UNITS': units}
df = DataFrame(data)
with open('./recipe_ingredient_table.json', 'w', encoding='utf-8') as file:
    df.to_json(file, force_ascii=False)


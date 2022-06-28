import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from pandas import DataFrame
import random

service = Service('./chromedriver.exe')
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

# 메뉴 정확순 정렬
# for menu in test_menu:
for menu in menu_list:
    url = f'https://www.10000recipe.com/recipe/list.html?q={menu}&query=&cat1=&cat2=&cat3=&cat4=&fct=&order=accuracy&lastcate=order&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
    driver.get(url)

    sleep(3)

    # 카테고리별 첫 번째 레시피
    recipe_xpath = '//*[@id="contents_area_full"]/ul/ul/li[1]/div[1]/a'
    recipe = driver.find_element(By.XPATH, recipe_xpath)
    recipe_url = recipe.get_attribute('href')
    print(menu, recipe_url)
    resp = requests.get(recipe_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    # n인분
    try:
        serving = soup.select_one('span[class=view2_summary_info1]').get_text()
        servings.append(serving)
    except:
        servings.append('1인분')

    # 재료, 수량
    ingredient = soup.select('#divConfirmedMaterialArea > ul')
    unit_n = list()
    igd_n = list()
    for i in range(len(ingredient)):
        unit_chd = ingredient[i].findChildren('span')
        for n in range(len(unit_chd)):
            unit_n.append(unit_chd[n].text)

        igd_chd = ingredient[i].findChildren('li')
        for j in igd_chd:
            j.find("span").decompose()
            try:
                j.find("img").decompose()
                j.find("a").decompose()
                j = j.text.replace("\n\n\n", "").rstrip()

            except:
                j = j.text.replace("\n", "").rstrip()

            igd_n.append(j)
    units.append(unit_n)
    ingredients.append(igd_n)

    # 레시피
    try:
        recipe = soup.select('div[class="media-body"]')
        recipe_n = list()
        for i in recipe:
            if i.has_attr('id'):
                recipe_n.extend(i)
        recipes.append(recipe_n)

        # 레시피 내부 태그 제거
        for j in range(len(recipes)):
            for n in range(len(recipes[j])):
                if type(recipes[j][n]) == bs4.element.Tag:
                    recipes[j][n] = recipes[j][n].text
                else:
                    pass

                # 레시피 단어, 공백 제거
                if len(recipes[j][n]) < 10:
                    del recipes[j][n]

    except:
        pass



# print(test_menu)
# print(menu_list, len(menu_list))
# print(servings, len(servings))
# print(recipes, len(recipes))
# print(ingredients, len(ingredients))
# print(units, len(units))


# 레시피 데이터프레임 - 메뉴명, 인분, 레시피
# data = {'RECIPE_NM': test_menu, 'QNT': servings, 'RECIPE': recipes}
data = {'RECIPE_NM': menu_list, 'QNT': servings, 'RECIPE': recipes}
df_recipe = DataFrame(data)


# 재료 데이터프레임 - 메뉴명, 재료, 용량
# data = {'RECIPE_NM': test_menu, 'INGREDIENTS': ingredients, 'UNITS': units}
data = {'RECIPE_NM': menu_list, 'INGREDIENTS': ingredients, 'UNITS': units}
df_ingd = DataFrame(data)


# json 변환
num = random.randint(1,100)
with open(f'./recipe_table_{num}.json', 'w', encoding='utf-8') as file:
    df_recipe.to_json(file, force_ascii=False)

with open(f'./recipe_ingredient_table_{num}.json', 'w', encoding='utf-8') as file:
    df_ingd.to_json(file, force_ascii=False)

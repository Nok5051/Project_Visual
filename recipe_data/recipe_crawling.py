import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pandas import DataFrame

driver = webdriver.Chrome(ChromeDriverManager().install())

categories = {53:"면/만두", 54:"국/탕", 55:"찌개", 56:"메인반찬", 61:"퓨전", 65:"양식"}
category_list = list()
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
    menu_a = soup.select('ul[class="tag_cont"] > li > a')
    for i in range(len(menu_a)):
        category_list.append(categories[category])
    menu_ul.extend(menu_a)

for menu in menu_ul:
    menu_list.append(menu.text)

# 메뉴 정확순 정렬
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

try:
    # \n 제거
    for j in range(len(recipes)):
        for n in range(len(recipes[j])):
            recipes[j][n] = recipes[j][n].replace("\n", "")
            recipes[j][n] = recipes[j][n] + "<br>"
    # 리스트 join
    for j in range(len(recipes)):
        recipes[j] = ' '.join(recipes[j])

except:
    pass

# 레시피 데이터프레임 - 메뉴명, 인분, 레시피
data = {'RECIPE_NM': menu_list,"CATEGORY":category_list, 'QNT': servings, 'RECIPE': recipes, 'INGREDIENTS': ingredients, 'UNITS': units}
df_recipe = DataFrame(data)

# json 변환
with open('./recipe_data/recipe_table_br.json', 'w', encoding='utf-8') as file:
    df_recipe.to_json(file, force_ascii=False)

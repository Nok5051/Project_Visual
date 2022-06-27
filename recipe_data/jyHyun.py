import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import json

service = Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

categories = [53, 54, 55, 56, 61, 65]
menu_ul = list()
menu_list = list()
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

# print(menu_list) - 파스타, 라면 , ... 총 622개

# test_menu = menu_list[0:2]
# for menu in test_menu:

# 메뉴 정확순 정렬
for menu in menu_list:
    url = f'https://www.10000recipe.com/recipe/list.html?q={menu}&query=&cat1=&cat2=&cat3=&cat4=&fct=&order=accuracy&lastcate=order&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
    driver.get(url)
    sleep(3)

    # 첫 번째 레시피 - 재료, 단위, 레시피 크롤링
    recipe_xpath = '//*[@id="contents_area_full"]/ul/ul/li[1]/div[1]/a'
    recipe = driver.find_element(By.XPATH, recipe_xpath)
    recipe_url = recipe.get_attribute('href')
    print(recipe_url)
    resp = requests.get(recipe_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    ingredients.append(soup.select('#divConfirmedMaterialArea > ul > a > li'))
    units.append(soup.select('span[class="ingre_unit"]'))
    recipes.append(soup.select('div[class="media-body"]'))

# print(ingredients)
# print(units)
# print(recipes)

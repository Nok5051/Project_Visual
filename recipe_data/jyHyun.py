import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json

service = Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 음식 카테고리 > 메뉴 리스트
categories = [53, 54, 55, 56, 61, 65]
menu_ul = list()
menu_list = list()
for category in categories:
    target_url = f'https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4={category}&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
    resp = requests.get(target_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    menu_ul.extend(soup.select('ul[class="tag_cont"] > li > a'))
    for menu in menu_ul:
        menu_list.append(menu.text)
# print(menu_list) - 파스타, 라면 , ...
test_menu = menu_list[0:3]


# 정확순 정렬 메뉴 리스트 > 1번째 레시피 Xpath 클릭
for menu in test_menu:
# for menu in menu_list:
    
    url = f'https://www.10000recipe.com/recipe/list.html?q={menu}&query=&cat1=&cat2=&cat3=&cat4=&fct=&order=accuracy&lastcate=order&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
    driver.get(url)
    recipe_xpath = '//*[@id="contents_area_full"]/ul/ul/li[1]/div[1]/a/img'
    recipe = driver.find_element_by_xpath(recipe_xpath)
    recipe.click()


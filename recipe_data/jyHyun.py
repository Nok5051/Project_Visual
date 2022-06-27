import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

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
# print(menu_list)

# 정확순 정렬 메뉴 리스트 > 1번째 객체
for menu in menu_list:
    target_url = f'https://www.10000recipe.com/recipe/list.html?q={menu}&query=&cat1=&cat2=&cat3=&cat4=&fct=&order=accuracy&lastcate=order&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
    resp = requests.get(target_url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    top_menu = soup.select('ul[class="common_sp_list_ul ea4"] > li')[0]
    print(len(top_menu))

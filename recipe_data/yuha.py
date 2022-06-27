import requests
from xml.etree import ElementTree
import re

def ingredient_price():
    service_key = '446644484867773537346d57656372'
    url = f'http://openAPI.seoul.go.kr:8088/{service_key}/xml/ListNecessariesPricesService/1/5/'

    resp = requests.get(url)
    tree = ElementTree.fromstring(resp.text)
    for child in tree:
        print(child.tag, child.attrib)





if __name__ == '__main__':
    ingredient_price()
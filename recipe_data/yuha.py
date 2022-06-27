import requests
from xml.etree import ElementTree
import pandas as pd

def ingredient_price():
    service_key = '446644484867773537346d57656372'
    url = f'http://openAPI.seoul.go.kr:8088/{service_key}/xml/ListNecessariesPricesService/1/1000/'
    # print(url)
    resp = requests.get(url)
    tree = ElementTree.fromstring(resp.text)
    # print(tree[2][4].text)


    rows = []

    for row in range(2, 1000):
        m_name = tree[row].find('M_NAME').text
        a_name = tree[row].find('A_NAME').text
        a_unit = tree[row].find('A_UNIT').text
        a_price = tree[row].find('A_PRICE').text
        m_type_name = tree[row].find('M_TYPE_NAME').text
        m_gu_name = tree[row].find('M_GU_NAME').text

        rows.append({"시장/마트명":m_name,
                     "품목명":a_name,
                     "판매단위":a_unit,
                     "판매가격":a_price,
                     "시장유형":m_type_name,
                     "자치구":m_gu_name})

    columns = ["시장/마트명", "품목명", "판매단위", "판매가격", "시장유형", "자치구"]
    ingredient_price_df = pd.DataFrame(rows, columns = columns)

    print(ingredient_price_df.head(10))




if __name__ == '__main__':
    ingredient_price()
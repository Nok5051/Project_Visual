import requests
from xml.etree import ElementTree
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import config
import plotly.express as px

def ingredient_price_api():
    # 서울시 생필품 농수축산물 가격 정보
    # 토요일 오전에 업데이트 됨
    service_key = config.seoul_api_key
    # url = f'http://openAPI.seoul.go.kr:8088/{service_key}/xml/ListNecessariesPricesService/1/5/'
    # print(url)
    # resp = requests.get(url)
    # tree = ElementTree.fromstring(resp.text)
    # print(tree[0].text)
    get_data_round = 7

    rows = []

    for i in range(1, get_data_round + 1):
        start_data = (i - 1) * 1000 + 1
        end_data = i * 1000
        url2 = f'http://openAPI.seoul.go.kr:8088/{service_key}/xml/ListNecessariesPricesService/{start_data}/{end_data}/'
        resp = requests.get(url2)
        tree2 = ElementTree.fromstring(resp.text)
        # print(url2)
        for row in range(2, 1002):
            if tree2[row].find('P_YEAR_MONTH').text == '2022-06':
                m_code = tree2[row].find('M_SEQ').text
                m_name = tree2[row].find('M_NAME').text
                a_code = tree2[row].find('A_SEQ').text
                a_name = tree2[row].find('A_NAME').text
                a_unit = tree2[row].find('A_UNIT').text
                a_price = tree2[row].find('A_PRICE').text
                m_type_code = tree2[row].find('M_TYPE_CODE').text
                m_gu_name = tree2[row].find('M_GU_NAME').text

                rows.append({"시장/마트 코드":m_code,
                             "시장/마트 이름":m_name,
                             "품목코드":a_code,
                             "품목명":a_name,
                             "판매단위":a_unit,
                             "판매가격":a_price,
                             "시장유형":m_type_code, # 1 - 전통시장 / 2 - 대형마트
                             "자치구":m_gu_name})


    # columns = ["시장/마트 코드", "시장/마트명", "품목코드", "품목명", "판매단위", "판매가격", "시장유형", "자치구"]
    ingredient_price_df = pd.DataFrame(rows)

    # print(ingredient_price_df.head(10))
    return ingredient_price_df


def ingredient_price_crawling():
    # target_url = 'https://www.kpi.or.kr/www/life/info_detail.asp?CateCode=L001001&DateCode=2022064'
    # resp = urllib.request.urlopen(target_url)
    # print(resp)
    # soup = BeautifulSoup(resp, 'html.parser')

    #print(soup)

    # CateCode : L001001 ~ L001007 / L002001 ~ L002004
    # DateCode : 년월주 / 일단은 20220604(2022년 6월 4째주)
    rows = []
    # 전통시장 품목 가격 가져오기
    for i in range(1, 8):
        target_url = f"https://www.kpi.or.kr/www/life/info_detail.asp?CateCode=L00100{i}&DateCode=2022061"
        resp = urllib.request.urlopen(target_url)
        soup = BeautifulSoup(resp, 'html.parser')

        data_title = soup.find('tr', 'font_b_gray02')
        title_tags = data_title.select('td')
        columns = []
        for td in title_tags:
            title = td.text
            columns.append(title)
        columns = columns[0:3]

        data_tr = soup.select('.life-td-pa')
        for tr in data_tr:
            data_tags = tr.select('td')
            dict = {}
            for i in range(0, len(columns)):
                dict[columns[i]] = data_tags[i].text
            rows.append(dict)
    # 대형마트 품목 가격 가져오기
    for i in range(1, 4):
        target_url = f"https://www.kpi.or.kr/www/life/info_detail.asp?CateCode=L00200{i}&DateCode=2022061"
        resp = urllib.request.urlopen(target_url)
        soup = BeautifulSoup(resp, 'html.parser')

        data_title = soup.find('tr', 'font_b_gray02')
        title_tags = data_title.select('td')
        columns = []
        for td in title_tags:
            title = td.text
            columns.append(title)
        columns = columns[0:5]

        data_tr = soup.select('.life-td-pa')
        for tr in data_tr:
            data_tags = tr.select('td')
            dict = {}
            for i in range(0, len(columns)):
                dict[columns[i]] = data_tags[i].text
            rows.append(dict)
    # 즉석밥 가격 붙이기
    target_url = f"https://www.kpi.or.kr/www/life/info_detail.asp?CateCode=L002010&DateCode=2022061"
    resp = urllib.request.urlopen(target_url)
    soup = BeautifulSoup(resp, 'html.parser')

    data_title = soup.find('tr', 'font_b_gray02')
    title_tags = data_title.select('td')
    columns = []
    for td in title_tags:
        title = td.text
        columns.append(title)
    columns = columns[0:5]

    data_tr = soup.select('.life-td-pa')
    for tr in data_tr:
        data_tags = tr.select('td')
        dict = {}
        for i in range(0, len(columns)):
            dict[columns[i]] = data_tags[i].text
        rows.append(dict)


    ingredient_price_df = pd.DataFrame(rows)


    return ingredient_price_df


def get_kamis_data():
    service_key = config.kamis_api_key
    service_id = '2579'

    # 최근 일자 도.소매가격정보(상품 기준)
    url = f'http://www.kamis.or.kr/service/price/xml.do?action=dailyCountyList&p_cert_key={service_key}&p_cert_id={service_id}&p_returntype=xml&p_countycode=1101'
    resp = requests.get(url)
    tree = ElementTree.fromstring(resp.text)

    items = tree[2].findall('item')
    rows = []
    regday = tree[0][0][0].text
    for item in items:
        category_code = item.find('category_code').text
        category_name = item.find('category_name').text
        productno = item.find('productno').text
        productName = item.find('productName').text
        day = item.find('lastest_day').text
        unit = item.find('unit').text
        dpr1 = item.find('dpr1').text
        dpr2 = item.find('dpr2').text
        dpr3 = item.find('dpr3').text
        dpr4 = item.find('dpr4').text

        # 최근 가격추이(상품 기준 - 품목코드)
        url = f'http://www.kamis.or.kr/service/price/xml.do?action=recentlyPriceTrendList&p_productno={productno}&p_regday={day}&p_cert_key={service_key}&p_cert_id={service_id}&p_returntype=xml'
        resp = requests.get(url)
        tree = ElementTree.fromstring(resp.text)
        d10 = tree[2][0].find('d10').text
        d20 = tree[2][0].find('d20').text

        try:
            cost1 = int(dpr1.replace(',', ''))
            cost2 = int(dpr2.replace(',', ''))
            cost3 = int(dpr3.replace(',', ''))
            cost4 = int(dpr4.replace(',', ''))
            cost10 = int(d10.replace(',', ''))
            cost20 = int(d20.replace(',', ''))
        except:
            cost1 = 1
            cost2 = 1
            cost3 = 1
            cost4 = 1
            cost10 = 1
            cost20 = 1

        direction = -1 # 0: 가격하락 / 1: 가격상승 / 2: 등락없음 or 정보없음
        if(cost2/cost10 == 1):
            direction = 2
        elif(cost2/cost10 > 1):
            direction = 1
        else:
            direction = 0

        value = 0 # 등락률
        if(direction == 0):
            value = round(cost2/cost10, 2)
        elif(direction == 1):
            value = round(cost10/cost2, 2)
        else:
            value = 0


        rows.append({"부류코드": category_code,
                     "부류명": category_name,
                     "품목코드": productno,
                     "품목명": productName,
                     "단위": unit,
                     "당일": cost1,
                     "1일전": cost2,
                     "10일전": cost10,
                     "20일전": cost20,
                     "1개월전": cost3,
                     "1년전": cost4,
                     "등락": direction,
                     "등락률": value
                     })

    ingredient_prices = pd.DataFrame(rows)


    # ingredient_prices = ingredient_prices.fillna(0)
    # ingredient_prices = ingredient_prices.astype({'부류코드':'category', '부류명':'category','품목코드':'category', '품목명':'category'})
    # print(ingredient_prices['품목명'].values.categories)

    # visualization : 당일, 등락, 등락률 표시하고 / 1일전, 10일전, 20일전, 1개월전, 1년전 line graph
    # df_graph = ingredient_prices.iloc[0]
    # fig = px.line(df_graph, x=['1년전', '1개월전', '20일전', '10일전', '1일전', '당일'], y=[df_graph[10], df_graph[9], df_graph[8], df_graph[7], df_graph[6], df_graph[5]], title="Price")
    # fig.show()



if __name__ == '__main__':
    #df_api = ingredient_price_api()
    # print(df_api.head(10))
    #df_crawling = ingredient_price_crawling()
    #print(df_crawling)

    # df_api.to_csv('ingredient_price_1.csv', index=False, encoding='utf-8-sig')
    # df_crawling.to_csv('ingredient_price_2.csv', index=False, encoding='utf-8-sig')

    get_kamis_data()

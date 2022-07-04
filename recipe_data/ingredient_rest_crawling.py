import requests
from bs4 import BeautifulSoup
import csv



ingre_list = ["파스타면","올리브유","다진마늘","매실청","만두","모짜렐라치즈","핫바","수제비","사골육수","쫄면","스파게티소스","짜장면","우동면","어묵","청경채","굴소스","가쓰오부시","들기름","김치","매실액","베이컨","샐러리","견과류","다시다 육수","생크림","페페론치노","아보카도오일","쌀국수","레몬즙","파마산치즈","치킨스톡","포도주","새우젓","떡국떡","떡볶이떡","한약재료","생선","다시다","맛술","돼지뼈","우거지","들깨","소주","유자폰즈소스","참깨흑임자드레싱","황태","냉동꽃게","냉동새우","참치액","순두부","참치캔","연어캔","스팸","청국장","꽁치통조림","콩비지","김치전","우렁","고구마줄기","스리라차소스","생간","녹말가루","인삼","닭다리","닭똥집","치킨튀김가루","카레","꿀","골뱅이","진미채","개복숭아","순대","떡갈비","샐러드야채","탕수육소스","전분","목이버섯","바베큐소스","스테이크소스","크래미","크림치즈","라이스페이퍼","허브맛솔트","부침가루","주꾸미","코다리","올리브","라자냐","아스파라거스","리코타치즈","빵가루","바질","완두콩","새싹","또띠아","옥수수콘","아보카도","단호박","콘치즈","칵테일새우","소시지","체다치즈","케첩","햄버거번","슬라이스치즈","돈까스소스","스위트칠리소스","피클","스트링치즈","파슬리","연어","비트","오렌지주스","포도씨유","바게트빵","로즈마리","엑스트라버진호두오일","3분 미트볼","스프","마카로니","크래커","허브소금","핫소스"]

title = []
price = []

for a in ingre_list :
    target_url = f'https://browse.gmarket.co.kr/search?keyword={a}'
    print(a)
    resp = requests.get(target_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tag = soup.find('span', {'class' : 'text__item'})
    price_tag = soup.find('strong', {'class' : 'text text__value'})
    title_text = title_tag.text
    title.append(title_text)
    price_text = price_tag.text
    price.append(price_text)


# recipe_dic = dict(zip(title,price))
# with open('ingd_rest_price.csv', 'w', encoding="utf-8 sig") as f:
#     writer = csv.writer(f)
#     for k, v in recipe_dic.items():
#         writer.writerow([k, v])

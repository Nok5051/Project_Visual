import json, pandas as pd
import csv
import re
import ast

# 1. 크롤링 데이터 결측치 제거
def recipe_preprocess():
    with open('./recipe_data/recipe_table.json', 'rt', encoding='UTF8') as f:
        rc = json.loads(f.read())

    df_rc = pd.DataFrame(rc)

    # 재료 없음 정리 - 인덱스 그대로
    ingd_null = df_rc['INGREDIENTS'].isin([[]])
    df_rc = df_rc[~ingd_null]

    # 레시피 없음 정리
    recipe_null = df_rc['RECIPE'].isin([""])
    df_rc = df_rc[~recipe_null]

    # 중복 메뉴 정리
    df_rc = df_rc.drop_duplicates(['RECIPE_NM'], keep='first', ignore_index=True)

    # 레시피 재료 표준 딕셔너리
    std_key = ["우동","우동소스","오뚜기(3분미트볼)","혼다시","가지","간장","국간장","만능간장","양조간장","조림간장","진간장","집간장","갈치","감자","감자(中)","감자小","감자작은거","감자중","감자큰사이즈","개복숭아","건새우","새우가루","견과류","견과류가루","계란","계란노른자","달걀","고구마","고구마줄기","고사리","불린고사리","고추","아삭이고추","청고추","풋고추","고추장","고추장찌개","\u200b고추장","고운고춧가루","고추가루","고춧가루","굵은고춧가루","골뱅이","굴소스","김","김가루","김볶음","김장김치","김치","김치국물","김치양손","김치찌개","김칫국물","묵은김치","배추김치","신김치","김치부침개","모듬전","깨","깻잎","꽁치통조림","손질꽃게","꿀","낙지","냉동꽃게","냉동새우","냉동칵테일새우","녹말가루","녹말물","느라티버섯","느타리버섯","맛타리버섯","다시다","다시육수","디포리육수혹은","멸치다시육수","멸치육수","액상조미료","요리에한수","육수티백","소고기다시다","마른새우육수","한방팩","다시마","다시마5cmx5cm","다진마늘","단호박","닭","닭가슴살","닭갈비","닭고기","닭다리살","닭볶음탕","삼계탕용생닭","당근","당근채손으로","납작당면","당면","당면사리","당면설탕","잡채","대추","밤대추","굵은파","다진파","대파","설어놓은대파","파채", "대파어슷썬것", "카츠야로스까스동봉소스","동태","다진돼지고기","대패삼겹살","돈까스","돼지갈비","돼지고기","돼지고기간것","돼지고기다짐육","돼지고기등심","돼지고기앞다리","불고기","수육","카츠야로스까스","돼지뼈","된장","미소된장","시판된장","집된장","된장국","더프레시안행복한콩브런치두부감자","두부","두부김치","두부반모","포프리두부","들기름","들깨가루","들깻가루","떡갈비","떡","떡국","오뚜기우리쌀떡국떡","떡볶이","떡볶이떡","또띠아","또띠아피자","라면","라면사리","라면스프","삼양라면","신라면","진짜진짜(면)","라자냐","레몬","레몬즙","로즈마리","리코타치즈","간마늘","두쪽마늘다진것","마늘","마늘가루","통마늘","편마늘","편썬마늘","마요네즈","맥앤치즈","만두","오뚜기옛날왕만두","맛술","생강술","청주","매실액","매실엑기스","매실원액","매실청","멸치","멸치액젓","액젓","모짜렐라치즈","슬라이스모짜렐라치즈","피자치즈","목이버섯","무","무3cm","무우","채썬무", "무나박썬것", "뜨거운물","물","생수","물엿","미나리","만데기","건미역","미역국","미림","미원","미향","연두순","요리당","천연조미료","밀가루","피자도우","구운빵","식빵","바게트빵","치아바타(바게트)","바나나","바베큐소스(매운맛)","바지락","생바지락크게","바질","바질한","신선한바질잎","방울토마토","다진배","배","배추","배추잎","속배추","흰콩(백태)불린것","버섯","버터","베이컨","부추","부침가루","오코노미야끼","북어","브로콜리","비빔면","구운비트간것","비트","빵가루","사골육수","오뚜기옛날사골곰탕국물","육수","사과","사과배양파","상추","새송이버섯","어린잎채소","새우","중하","중하새우","새우젓","샐러드야채","비타민야채","샐러리","생간","다진생강","생강","생강가루","생강즙","통구맹이","생크림","휘핑크림","검은콩(서리태)","설탕","원당","국거리소고기","등심스테이크","소갈비","소고기","소고기다짐육","소고기샤브샤브","소고기양지머리","소고기차돌박이","소불고기","쇠고기","쇠고기다진것","스테이크","안심스테이크","양지","프로슈토","함박스테이크","굵은소금","깨소금","꽃소금","소금","소금(입맛에맞게)","소금반","천일염","국수","소면","잔치국수","소시지","소주","수제비","숙주","숙주나물","숙주크게","순대","순두부","스리라차소스","스리랏차","스위트칠리소스","스테이크소스","스트링치즈","백설토마토파스타소스","스파게티소스","시판용토마토소스","시판크림스파게티소스","오뚜기프레스코스파게티소스토마토","크림소스","토마토소스","토마토파스타소스","토마토파스타소스(약225g)","스팸","스팸큰사이즈","진짜진짜(스프)","슬라이스고다치즈","3층치즈","시금치","식용유","요리유","튀김용기름","식초","쌀","쌀국수","월남쌈","쑥갓","슬라이스아몬드","아보카도","아보카도오일","아스파라거스","애호박","양배추","양배추채썰어서","적양패주","적채","양상추","양송이","양송이버섯","다진양파","양파","양파작은거","적양파","사각어묵","어묵","연어","연어캔","오렌지껍질","오렌지주스","오이","물오징어","오징어","옥수수","옥수수콘","올리고당","블랙올리브슬라이스","올리브","엑스트라버진올리브오일","올리브오일","올리브유","완두콩","우거지","우동면","우렁","우유","유자폰즈소스","인삼","감자전분","전분","조개살","주꾸미","진미채","짜장면","짬뽕","쪽파","쫄면","쫄면사리","참기름","창참기름","참깨","통깨","참깨흑임자드레싱","참치액","참치액젖","참치","참치캔기름","캔참치","찹쌀","찹쌀가루","청경채","청국장","매운고추","붉은고추","청량고추","청양고추","청양초","청홍고추","홍고추","체다슬라이즈치즈","체다치즈","체더슬라이스","슬라이스치즈","치즈","치킨스톡","카레","카레가루","칵테일새우","칼국수","케찹","케첩","냉동코다리","콘치즈","콩가루","콩나물","비지","크래미","크래커","크림치즈","백설탕수소스","잘익은토마토","토마토","파","치즈가루","파마산치즈","파마산치즈가루","스파게티","스파게티면","스파게티면손가락","파스타","파스타면","파슬리","파슬리가루","파프리카","팽이버섯","팽이버섯작은것","페퍼론치노","페페로치노","페페론치노","포도씨유","레드와인","백포도주","화이트와인","불린표고버섯","생표고보섯","표고버섯","붉은피망","청피망","피망","피망&파프리카","홍피망","오이피클","한약재료","핫바","핫소스","해바라기씨","더프레시안건강한브런치후랑크리치치즈","햄","햄버거번","햄버거번or모닝롤","밥","밥숟가락","햇반","쌀","허브맛솔트","허브소금","봄내음이호박","쥬키니호박","쥬키니호박나박썬것","호박","호박등각종(없음생략)","홍합","홍합탕","황태","황태머리","통후추","통후추약간등(","후추","후추가루","후추소금","후춧가루","훗추가루","흑후추가루","국남은것","국자","담을접시","비닐팩","쌀뜨물","쌀뜬물","원하는재료","큰그릇"]
    std_value = ["우동면", "간장", "3분 미트볼","가쓰오부시","가지","간장","간장","간장","간장","간장","간장","간장","갈치","감자","감자","감자","감자","감자","감자","개복숭아","건새우","건새우","견과류","견과류","계란","계란","계란","고구마","고구마줄기","고사리","고사리","고추","고추","고추","고추","고추장","고추장","고추장","고춧가루","고춧가루","고춧가루","고춧가루","골뱅이","굴소스","김","김","김","김치","김치","김치","김치","김치","김치","김치","김치","김치","김치전","김치전","깨","깻잎","꽁치통조림","꽃게","꿀","낙지","냉동꽃게","냉동새우","냉동새우","녹말가루","녹말가루","느타리버섯","느타리버섯","느타리버섯","다시다","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시마","다시마","다진마늘","단호박","닭고기","닭고기","닭고기","닭고기","닭고기","닭고기","닭고기","당근","당근","당면","당면","당면","당면","당면","대추","대추","대파","대파","대파","대파","대파","대파","돈까스소스","동태","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지뼈","된장","된장","된장","된장","된장","두부","두부","두부","두부","두부","들기름","들깨","들깨","떡갈비","떡국떡","떡국떡","떡국떡","떡볶이떡","떡볶이떡","또띠아","또띠아","라면","라면","라면","라면","라면","라면","라자냐","레몬","레몬즙","로즈마리","리코타치즈","마늘","마늘","마늘","마늘","마늘","마늘","마늘","마요네즈","마카로니","만두","만두","맛술","맛술","맛술","매실액","매실액","매실액","매실청","멸치","멸치액젓","멸치액젓","모짜렐라치즈","모짜렐라치즈","모짜렐라치즈","목이버섯","무","무","무","무", "무", "물","물","물","물엿","미나리","미더덕","미역","미역","미원","미원","미원","미원","미원","미원","밀가루","밀가루","바게트빵","바게트빵","바게트빵","바게트빵","바나나","바베큐소스","바지락","바지락","바질","바질","바질","방울토마토","배","배","배추","배추","배추","백태","버섯","버터","베이컨","부추","부침가루","부침가루","북어","브로콜리","비빔면","비트","비트","빵가루","사골육수","사골육수","사골육수","사과","사과","상추","새송이버섯","새싹","새우","새우","새우","새우젓","샐러드야채","샐러드야채","샐러리","생간","생강","생강","생강","생강","생선","생크림","생크림","서리태","설탕","설탕","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소금","소금","소금","소금","소금","소금","소금","소면","소면","소면","소시지","소주","수제비","숙주","숙주","숙주","순대","순두부","스리라차소스","스리라차소스","스위트칠리소스","스테이크소스","스트링치즈","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스팸","스팸","스프","슬라이스치즈","슬라이스치즈","시금치","식용유","식용유","식용유","식초","쌀","쌀국수","라이스페이퍼","쑥갓","아몬드","아보카도","아보카도오일","아스파라거스","애호박","양배추","양배추","양배추","양배추","양상추","양송이버섯","양송이버섯","양파","양파","양파","양파","어묵","어묵","연어","연어캔","오렌지","오렌지주스","오이","오징어","오징어","옥수수","옥수수콘","올리고당","올리브","올리브","올리브유","올리브유","올리브유","완두콩","우거지","우동면","우렁","우유","유자폰즈소스","인삼","전분","전분","조개","주꾸미","진미채","짜장면","짬뽕","쪽파","쫄면","쫄면","참기름","참기름","참깨","참깨","참깨흑임자드레싱","참치액","참치액","참치캔","참치캔","참치캔","찹쌀","찹쌀","청경채","청국장","청양고추","청양고추","청양고추","청양고추","청양고추","청양고추","청양고추","체다치즈","체다치즈","체다치즈","치즈","치즈","치킨스톡","카레","카레","칵테일새우","칼국수","케첩","케첩","코다리","콘치즈","콩","콩나물","콩비지","크래미","크래커","크림치즈","탕수육소스","토마토","토마토","파","파마산치즈","파마산치즈","파마산치즈","파스타면","파스타면","파스타면","파스타면","파스타면","파슬리","파슬리","파프리카","팽이버섯","페페론치노","페페론치노","페페론치노","페페론치노","포도씨유","포도주","포도주","포도주","표고버섯","표고버섯","표고버섯","피망","피망","피망","피망","피망","피클","한약재료","핫바","핫소스","해바라기씨","햄","햄","햄버거번","햇반","햇반","햇반","햇반","햇반","허브맛솔트","허브맛솔트","호박","호박","호박","호박","호박","홍합","홍합","황태","황태","후추","후추","후추","후추","후추","후추","후추","후추","남은 국","국자","접시","비닐팩","쌀뜨물","쌀뜨물","원하는 재료","그릇"]
    std_ingd = dict(zip(std_key, std_value))

    std_ingd = dict(zip(std_key, std_value))

    # 띄어쓰기 없애기, 표준 명칭으로 변경
    for ingredient in df_rc['INGREDIENTS']:
        for j in range(len(ingredient)):
            ingredient[j] = ingredient[j].replace(" ", "")
            try:
                ingredient[j] = std_ingd[ingredient[j]]
            except:
                pass

    # 재료 수량 ''값 처리 : 1
    for recipe in df_rc['UNITS']:
        for j in range(len(recipe)):
            if recipe[j] == '':
                recipe[j] = "1"

    # df_rc.to_csv("./recipe_data/df_rc.csv", encoding='utf-8-sig', header = 0)

    return df_rc



# 2. data_preprocessing.py - standard_price.csv 매칭 작업 
def standard_convert():
    df_rc = recipe_preprocess()
    unit_key = []
    for i in df_rc["INGREDIENTS"]:
        unit_key.append(i)  # [['파스타면', '물', '올리브유'], ['라면', '대파', '계란']]

    unit_value = []
    for i in df_rc["UNITS"]:
        unit_value.append(i)  # [['1', '1', '1'], ['1개', '조금', '1개']]

    # 표준 단위 CSV와 단위 맞추기 (수작업 - json으로 만들기)
    # 수작업 파일 불러오기
    df_unit = pd.read_csv("./recipe_data/ingd-unit_check_fin.csv")
    print("파일 불러오기 성공")

    # UNITS 값 리스트 변환
    for i in range(len(df_unit["UNITS"])):
        x = df_unit["UNITS"][i]
        x = ast.literal_eval(x)
        df_unit["UNITS"][i] = x

    print("UNITS 리스트 변환 성공")


    # 재료-unit 맞춰서 데이터프레임 넣기
    for i in range(len(df_rc["INGREDIENTS"])): # 메뉴 숫자만큼
        # print("i : ", i)
        for j in range(len(df_rc["INGREDIENTS"][i])): # 메뉴의 재료 숫자만큼
            # print("j : ", j)
            for n in range(len(df_unit["INGREDIENT"])):
                if df_rc["INGREDIENTS"][i][j] == df_unit["INGREDIENT"][n]:
                    # print("n : ", df_unit["INGREDIENT"][n])
                    df_rc["UNITS"][i][j] = df_unit["UNITS"][n].pop(0)
    
    return df_rc

# 3. 레시피별 총 금액 계산
def total_calculate():
    df_rc = standard_convert()
    # 총 가격 계산
    df_ing = pd.read_csv('./recipe_data/standard_price.csv')
    print("가격 계산 시작")

    df_price = df_rc.copy()

    total_price = []
    for i in range(0, len(df_price)):
        ingredients = df_price.iloc[i]['INGREDIENTS']
        units = df_price.iloc[i]['UNITS']
        price = []
        for item in ingredients:
            temp_df = df_ing[df_ing['name'] == item]
            if(len(temp_df) != 0):
                price.append(int(temp_df['price'].values))
        price_sum = 0
        for j in range(0, len(price)):
            price_sum += eval(units[j]) * price[j]
        total_price.append(round(price_sum))

    df_price["TOTAL_PRICE"] = total_price
    print("가격 계산 완료")

    # 재료 list to string
    for i in range(len(df_rc['INGREDIENTS'])): # df_rc.iloc[i]['INGREDIENTS'] = ['파스타면', '물', '올리브유']
        df_rc.iloc[i]['INGREDIENTS'] = ", ".join(df_rc.iloc[i]['INGREDIENTS'])

    print("재료 리스트 변환 완료")

    df_rc["TOTAL_PRICE"] = df_price["TOTAL_PRICE"]

    # csv export
    df_rc.to_csv("./recipe_data/df_rc.csv", encoding='utf-8-sig', header = 0)
    print("파일 변환 완료")
    return df_rc

if __name__ == '__main__':
    total_calculate()
import json, pandas as pd

# 크롤링 데이터 불러오기
with open('recipe_ingredient_table_all.json','rt', encoding='UTF8') as f:
    igd = json.loads(f.read())

with open('recipe_table_all.json', 'rt', encoding='UTF8') as f:
    rc = json.loads(f.read())

df_igd = pd.DataFrame(igd)
df_rc = pd.DataFrame(rc)

# 중복 메뉴 정리 -
df_rc = df_rc.drop_duplicates(['RECIPE_NM'], keep='first', ignore_index=True)
df_igd = df_igd.drop_duplicates(['RECIPE_NM'], keep='first', ignore_index=True)

# 재료 없음 정리 - 인덱스 그대로
ingd_null = df_igd['INGREDIENTS'].isin([[]])
# print(ingd_null.sum())
df_igd = df_igd[~ingd_null]


# 레시피 없음 정리 : df_rc 153개, df_igd 160개
recipe_null = df_rc['RECIPE'].isin([[]])
# print(recipe_null.sum())
df_rc = df_rc[~recipe_null]

# 레시피 재료 표준 딕셔너리
key = ["오뚜기(3분미트볼)","혼다시","가지","간장","국간장","만능간장","양조간장","조림간장","진간장","집간장","갈치","감자","감자(中)","감자小","감자작은거","감자중","감자큰사이즈","개복숭아","건새우","새우가루","견과류","견과류가루","계란","계란노른자","달걀","고구마","고구마줄기","고사리","불린고사리","고추","아삭이고추","청고추","풋고추","고추장","고추장찌개","고운고춧가루","고추가루","고춧가루","굵은고춧가루","골뱅이","굴소스","김","김가루","김볶음","김장김치","김치","김치국물","김치양손","김치찌개","김칫국물","묵은김치","배추김치","신김치","김치부침개","모듬전","깨","깻잎","꽁치통조림","손질꽃게","꿀","낙지","냉동꽃게","냉동새우","냉동칵테일새우","녹말가루","녹말물","느라티버섯","느타리버섯","맛타리버섯","다시다","다시육수","디포리육수혹은","멸치다시육수","멸치육수","액상조미료","요리에한수","육수티백","한방팩","다시마","다시마5cmx5cm","다진마늘","단호박","닭","닭가슴살","닭갈비","닭고기","닭다리살","닭볶음탕","삼계탕용생닭","당근","당근채손으로","납작당면","당면","당면사리","당면설탕","잡채","대추","밤대추","굵은파","다진파","대파","설어놓은대파","파채","카츠야로스까스동봉소스","동태","다진돼지고기","대패삼겹살","돈까스","돼지갈비","돼지고기","돼지고기간것","돼지고기다짐육","돼지고기등심","돼지고기앞다리","불고기","수육","카츠야로스까스","돼지뼈","된장","미소된장","시판된장","집된장","된장국","더프레시안행복한콩브런치두부감자","두부","두부김치","두부반모","포프리두부","들기름","들깨가루","들깻가루","떡갈비","떡","떡국","오뚜기우리쌀떡국떡","떡볶이","떡볶이떡","또띠아","또띠아피자","라면","라면사리","라면스프","삼양라면","신라면","진짜진짜(면)","라자냐","레몬","레몬즙","로즈마리","리코타치즈","간마늘","두쪽마늘다진것","마늘","마늘가루","통마늘","편마늘","편썬마늘","마요네즈","맥앤치즈","만두","오뚜기옛날왕만두","맛술","생강술","청주","매실액","매실엑기스","매실원액","매실청","멸치","멸치액젓","액젓","모짜렐라치즈","슬라이스모짜렐라치즈","피자치즈","목이버섯","무","무3cm","무우","채썬무","뜨거운물","물","생수","물엿","미나리","만데기","건미역","미역국","미림","미원","미향","소고기다시다","연두순","요리당","천연조미료","밀가루","피자도우","구운빵","바게트빵","치아바타(바게트)","바나나","바베큐소스(매운맛)","바지락","생바지락크게","바질","바질한","신선한바질잎","방울토마토","다진배","배","배추","배추잎","속배추","흰콩(백태)불린것","버섯","버터","베이컨","부추","부침가루","오코노미야끼","북어","브로콜리","비빔면","구운비트간것","비트","빵가루","사골육수","오뚜기옛날사골곰탕국물","육수","사과","사과배양파","상추","새송이버섯","어린잎채소","새우","중하","중하새우","새우젓","샐러드야채","비타민야채","샐러리","생간","다진생강","생강","생강가루","생강즙","통구맹이","생크림","휘핑크림","검은콩(서리태)","설탕","원당","국거리소고기","등심스테이크","소갈비","소고기","소고기다짐육","소고기샤브샤브","소고기양지머리","소고기차돌박이","소불고기","쇠고기","쇠고기다진것","스테이크","안심스테이크","양지","프로슈토","함박스테이크","굵은소금","깨소금","꽃소금","소금","소금(입맛에맞게)","소금반","천일염","국수","소면","잔치국수","소시지","소주","수제비","숙주","숙주나물","숙주크게","순대","순두부","스리라차소스","스리랏차","스위트칠리소스","스테이크소스","스트링치즈","백설토마토파스타소스","스파게티소스","시판용토마토소스","시판크림스파게티소스","오뚜기프레스코스파게티소스토마토","크림소스","토마토소스","토마토파스타소스","토마토파스타소스(약225g)","스팸","스팸큰사이즈","진짜진짜(스프)","슬라이스고다치즈","시금치","식빵","식용유","요리유","튀김용기름","식초","쌀","쌀국수","월남쌈","쑥갓","슬라이스아몬드","아보카도","아보카도오일","아스파라거스","애호박","양배추","양배추채썰어서","적양패주","적채","양상추","양송이","양송이버섯","다진양파","양파","양파작은거","적양파","사각어묵","어묵","연어","연어캔","오렌지껍질","오렌지주스","오이","물오징어","오징어","옥수수","옥수수콘","올리고당","블랙올리브슬라이스","올리브","엑스트라버진올리브오일","올리브오일","올리브유","완두콩","우거지","우동면","우렁","우유","유자폰즈소스","인삼","감자전분","전분","조개살","주꾸미","진미채","짜장면","짬뽕","쪽파","쫄면","쫄면사리","참기름","창참기름","참깨","통깨","참깨흑임자드레싱","참치액","참치액젖","참치","참치캔기름","캔참치","찹쌀","찹쌀가루","청경채","청국장","매운고추","붉은고추","청량고추","청양고추","청양초","청홍고추","홍고추","체다슬라이즈치즈","체다치즈","체더슬라이스","슬라이스치즈","치즈","치킨스톡","카레","카레가루","칵테일새우","칼국수","케찹","케첩","냉동코다리","콘치즈","콩가루","콩나물","비지","크래미","크래커","크림치즈","백설탕수소스","잘익은토마토","토마토","파","치즈가루","파마산치즈","파마산치즈가루","스파게티","스파게티면","스파게티면손가락","파스타","파스타면","파슬리","파슬리가루","파프리카","팽이버섯","팽이버섯작은것","페퍼론치노","페페로치노","페페론치노","포도씨유","레드와인","백포도주","화이트와인","불린표고버섯","생표고보섯","표고버섯","붉은피망","청피망","피망","피망&파프리카","홍피망","오이피클","한약재료","핫바","핫소스","해바라기씨","더프레시안건강한브런치후랑크리치치즈","햄","햄버거번","햄버거번or모닝롤","밥","밥숟가락","햇반","허브맛솔트","봄내음이호박","쥬키니호박","호박","호박등각종(없음생략)","홍합","홍합탕","황태","황태머리","통후추","통후추약간등(","후추","후추가루","후추소금","후춧가루","훗추가루","흑후추가루","국남은것","국자","담을접시","비닐팩","쌀뜨물","쌀뜬물","원하는재료","큰그릇"]
value = ["3분 미트볼","가쓰오부시","가지","간장","간장","간장","간장","간장","간장","간장","갈치","감자","감자","감자","감자","감자","감자","개복숭아","건새우","건새우","견과류","견과류","계란","계란","계란","고구마","고구마줄기","고사리","고사리","고추","고추","고추","고추","고추장","고추장","고춧가루","고춧가루","고춧가루","고춧가루","골뱅이","굴소스","김","김","김","김치","김치","김치","김치","김치","김치","김치","김치","김치","김치전","김치전","깨","깻잎","꽁치통조림","꽃게","꿀","낙지","냉동꽃게","냉동새우","냉동칵테일새우","녹말가루","녹말가루","느타리버섯","느타리버섯","느타리버섯","다시다","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시마","다시마","다진마늘","단호박","닭고기","닭고기","닭고기","닭고기","닭고기","닭고기","닭고기","당근","당근","당면","당면","당면","당면","당면","대추","대추","대파","대파","대파","대파","대파","돈까스소스","동태","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지뼈","된장","된장","된장","된장","된장","두부","두부","두부","두부","두부","들기름","들깨","들깨","떡갈비","떡국떡","떡국떡","떡국떡","떡볶이떡","떡볶이떡","또띠아","또띠아","라면","라면","라면","라면","라면","라면","라자냐","레몬","레몬즙","로즈마리","리코타치즈","마늘","마늘","마늘","마늘","마늘","마늘","마늘","마요네즈","마카로니","만두","만두","맛술","맛술","맛술","매실액","매실액","매실액","매실청","멸치","멸치액젓","멸치액젓","모짜렐라치즈","모짜렐라치즈","모짜렐라치즈","목이버섯","무","무","무","신","물","물","물","물엿","미나리","미더덕","미역","미역","미원","미원","미원","미원","미원","미원","미원","밀가루","밀가루","바게트빵","바게트빵","바게트빵","바나나","바베큐소스","바지락","바지락","바질","바질","바질","방울토마토","배","배","배추","배추","배추","백태","버섯","버터","베이컨","부추","부침가루","부침가루","북어","브로콜리","비빔면","비트","비트","빵가루","사골육수","사골육수","사골육수","사과","사과","상추","새송이버섯","새싹","새우","새우","새우","새우젓","샐러드야채","샐러드야채","샐러리","생간","생강","생강","생강","생강","생선","생크림","생크림","서리태","설탕","설탕","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소금","소금","소금","소금","소금","소금","소금","소면","소면","소면","소시지","소주","수제비","숙주","숙주","숙주","순대","순두부","스리라차소스","스리라차소스","스위트칠리소스","스테이크소스","스트링치즈","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스팸","스팸","스프","슬라이스치즈","시금치","식빵","식용유","식용유","식용유","식초","쌀","쌀국수","라이스페이퍼","쑥갓","아몬드","아보카도","아보카도오일","아스파라거스","애호박","양배추","양배추","양배추","양배추","양상추","양송이버섯","양송이버섯","양파","양파","양파","양파","어묵","어묵","연어","연어캔","오렌지","오렌지주스","오이","오징어","오징어","옥수수","옥수수콘","올리고당","올리브","올리브","올리브유","올리브유","올리브유","완두콩","우거지","우동면","우렁","우유","유자폰즈소스","인삼","전분","전분","조개","주꾸미","진미채","짜장면","짬뽕","쪽파","쫄면","쫄면","참기름","참기름","참깨","참깨","참깨흑임자드레싱","참치액","참치액","참치캔","참치캔","참치캔","찹쌀","찹쌀","청경채","청국장","청양고추","청양고추","청양고추","청양고추","청양고추","청양고추","청양고추","체다치즈","체다치즈","체다치즈","치즈","치즈","치킨스톡","카레","카레","칵테일새우","칼국수","케첩","케첩","코다리","콘치즈","콩","콩나물","콩비지","크래미","크래커","크림치즈","탕수육소스","토마토","토마토","파","파마산치즈","파마산치즈","파마산치즈","파스타면","파스타면","파스타면","파스타면","파스타면","파슬리","파슬리","파프리카","팽이버섯","페페론치노","페페론치노","페페론치노","페페론치노","포도씨유","포도주","포도주","포도주","표고버섯","표고버섯","표고버섯","피망","피망","피망","피망","피망","피클","한약재료","핫바","핫소스","해바라기씨","햄","햄","햄버거번","햇반","햇반","햇반","햇반","허브맛솔트","호박","호박","호박","호박","홍합","홍합","황태","황태","후추","후추","후추","후추","후추","후추","후추","후추","","","","","","","",""]
std_ingd = dict(zip(key, value))

std_unit = dict(zip(key, value))

for ingredient in df_igd['INGREDIENTS']:
    # print(ingredient, type)
    for j in range(len(ingredient)):
        ingredient[j] = ingredient[j].replace(" ", "")
        try:
            ingredient[j] = std_ingd[ingredient[j]]
        except:
            pass


# 재료 수량 null -> 1 넣기
for recipe in df_igd['UNITS']:
    # print(ingredient, type)
    for j in range(len(recipe)):
        if recipe[j] == '':
            recipe[j] = 1

# print(df_igd['INGREDIENTS'])
# df_igd.to_csv("df_igd_std_2.csv", encoding='utf-8-sig')


# 재료별 용량법 확인
# key = [['파스타면', '물', '올리브유'],['라면', '대파', '계란'],['김', '배', '양배추', '부추', '소고기', '간장', '설탕', '대파', '다진마늘', '후추', '배', '양파', '대파', '마늘', '고추장', '간장', '매실청', '식초', '설탕', '고춧가루', '참기름', '참깨'],['만두'],['파스타면', '고구마', '모짜렐라치즈', '치즈', '핫바', '방울토마토'],['소면', '소고기', '계란', '호박', '당근', '간장', '소금', '마늘', '고춧가루', '참기름'],['소면', '된장', '오이', '소금', '참기름'],['수제비', '감자', '양파', '청양고추', '당근', '호박', '멸치액젓', '사골육수', '김', '소금'],['칼국수', '당근', '양파', '호박', '부추', '대파', '물', '간장', '다진마늘', '후추', '소금'],['쫄면', '상추', '참기름', '식초', '고추장', '설탕'],['파스타면', '햄', '양파', '스파게티소스', '우유'],['백태', '소금', '소면', '오이', '토마토'],['닭고기', '양배추', '양파', '당근', '대파', '짜장면', '미원', '생강', '후추', '멸치액젓', '참기름', '고춧가루'],['우동면', '어묵', '숙주', '청경채', '양배추', '대파', '굴소스'],['새우', '홍합', '오징어', '양파', '당근', '소금', '고춧가루', '배추', '숙주', '물', '짬뽕', '가쓰오부시', '다진마늘', '후추'],['비빔면', '계란', '청양고추', '대파', '들기름', '참깨'],['귤', '우동'],['김치', '소면', '다진마늘', '고추장', '참기름', '간장', '매실액', '설탕', '소금'],['파스타면', '스파게티소스', '베이컨', '양파', '계란', '우유'],['스파게티소스', '파스타면', '양파', '브로콜리', '느타리버섯', '베이컨', '방울토마토'],['양파', '당근', '샐러리', '파프리카', '소면', '간장', '참기름', '설탕', '고추장', '마늘', '고춧가루', '설탕', '참기름', '매실액', '견과류'],['냉면', '계란', '소고기', '물김치', '소금', '참기름'],['다시다 육수', '애호박', '감자', '대파', '청양고추', '청양고추', '바지락', '라면'],['마늘', '양파', '베이컨', '소금', '파스타면', '우유', '생크림', '치즈', '버터'],['파스타면', '양파', '페페론치노', '파프리카', '마늘', '아보카도오일', '소금', '후추'],['라면', '햄', '대파', '계란'],['쌀국수', '사골육수', '소고기', '숙주', '양파', '청양고추', '레몬즙', '멸치액젓', '햇반'],['파스타면', '피망', '양파', '새우', '스파게티소스', '올리브유', '소금', '마늘'],['파스타면', '페페론치노', '마늘', '소금', '후추', '파마산치즈', '치킨스톡', '포도주'],['소고기', '무', '물', '다시마', '간장', '소금', '참기름', '다진마늘', '대파'],['미역', '물', '라면'],['닭고기', '콩나물', '참기름', '참깨', '햇반', '김'],['소고기', '미역', '다진마늘', '참기름', '멸치액젓', '소금'],['콩나물', '물', '새우젓', '대파', '다진마늘', '청양고추', '후추', '소금'],['멸치', '무', '감자', '느타리버섯', '양배추', '배추', '대파', '떡국떡', '된장', '다진마늘'],['떡국떡', '다시다 육수', '대파', '계란', '김', '소금'],['어묵', '계란', '떡볶이떡', '쑥갓', '표고버섯'],['닭고기', '마늘', '찹쌀', '한약재료', '대파'],['계란', '대파', '사골육수'],['소고기', '물', '고사리', '숙주', '대파', '무', '간장', '고춧가루', '참기름', '다진마늘', '소금', '후추'],['생선', '호박', '청양고추', '파', '버섯', '무', '된장'],['만두', '계란', '대파', '다시다 육수', '멸치액젓'],['떡국떡', '만두', '사골육수', '물', '다진마늘', '계란', '후추'],['', '', '', ''],['꽃게', '양파', '대파', '청양고추', '청양고추', '무', '물', '고춧가루', '소금', '다시다', '다진마늘', '미원', '된장', '후추', '미원'],['시금치', '두부', '느타리버섯', '건새우', '마늘', '물', '된장'],['배추', '양파', '대파', '청양고추', '청양고추', '두부', '물', '된장', '고춧가루', '다진마늘', '미원'],['오이', '양파', '청양고추', '청양고추', '설탕', '소금', '멸치액젓', '매실청', '간장', '식초', '레몬즙', '물'],['오징어', '무', '다시다 육수', '다시마', '양파', '다진마늘', '고춧가루', '소금', '맛술'],['감자', '애호박', '대파', '다시다 육수', '다진마늘', '간장', '소금', '후추'],['닭고기', '다시다 육수', '마늘', '생강', '오렌지', '물', '소금', '후추', '소금'],['북어', '신', '청양고추', '청양고추', '대파', '마늘', '다시다 육수', '계란', '간장', '소금', '후추', '참기름'],['돼지뼈', '감자', '우거지', '깻잎', '대파', '양파', '청양고추', '미원', '들깨', '소금', '소주', '된장', '고춧가루', '마늘', '생강', '후추'],['홍합', '물', '맛술', '대파', '청양고추', '소금'],['소고기', '배추', '깻잎', '청경채', '표고버섯', '느타리버섯', '다시다 육수', '유자폰즈소스', '소금', '후추', '간장', '참깨흑임자드레싱'],['콩나물', '김치', '다진마늘', '대파'],['황태', '무', '참기름', '소금', '간장', '식용유', '두부', '계란', '대파', '간장', '마늘'],['어묵', '당근', '양파', '대파', '청양고추', '소금', '미원'],['닭고기', '고사리', '대파', '청양고추', '다진마늘', '고춧가루', '간장', '후추', '참기름', '소금'],['냉동꽃게', '냉동새우', '표고버섯', '호박', '양파', '대파', '두부', '된장', '된장', '다진마늘', '참치액'],['돼지고기', '김치', '다시다 육수', '대파', '들기름'],['순두부', '양파', '대파', '계란', '다시다 육수', '다진마늘', '고춧가루', '참기름', '돼지고기', '다시다 육수', '건새우', '간장', '소금'],['고추장', '참치캔', '햇반', '애호박', '감자', '양파', '대파', '김'],['돼지고기', '양파', '대파', '두부', '김치', '햄', '고춧가루', '간장', '마늘', '소금', '후추'],['연어캔', '감자', '스팸', '양파', '두부', '호박', '김치', '대파', '청양고추', '물', '', '고추장', '김치', '참치액', '고춧가루'],['김치', '두부', '대파', '청양고추', '참치캔', '설탕', '참치액', '고추장', '고춧가루', '참치캔', '물'],['청국장', '양파', '파', '고추', '호박', '멸치액젓', '소금', '설탕'],['두부', '양파', '당근', '파', '다시마', '새우젓', '후추', '간장', '고춧가루'],['동태', '두부', '콩나물', '부추', '쑥갓', '대파', '바지락', '청양고추', '청양고추', '고춧가루', '맛술', '생강', '마늘', '소금', '멸치액젓', '후추', '다시마', '황태', '멸치', '건새우', '무', '양파', '청양고추', '대파', '물'],['소고기', '호박', '양파', '표고버섯', '팽이버섯', '대파', '청양고추', '두부', '다시다 육수', '된장', '고춧가루'],['스팸', '감자', '양파', '청양고추', '파', '물', '된장', '간장', '고추장', '고춧가루', '다진마늘', '맛술', '설탕'],['서리태', '돼지고기', '김치', '양파', '애호박', '고추', '청양고추', '쪽파', '물', '식용유', '고춧가루', '다진마늘', '맛술', '새우젓'],['돼지고기', '후추', '김치', '김치', '물', '간장', '생강', '매실액', '양파', '감자', '호박', '대파', '청양고추', '청양고추', '다진마늘', '고춧가루'],['김치', '꽁치통조림', '양파', '대파', '청양고추', '두부', '고춧가루', '설탕'],['돼지고기', '감자', '호박', '양파', '청양고추', '청양고추', '파', '다진마늘', '고추장', '고춧가루', '간장', '후추', '다시마', '멸치'],['콩비지', '김치', '돼지고기', '고추', '청양고추', '들기름', '다진마늘', '후추', '멸치액젓', '고춧가루'],['호박', '양파', '두부', '고추', '된장', '다시다 육수'],['햄', '파프리카', '호박', '버섯', '양파', '가지', '계란', '올리브유', '두부', '스파게티소스', '소금', '후추'],['감자', '돼지고기', '느타리버섯', '양파', '대파', '고추', '물', '참기름', '식용유', '고추장', '고춧가루', '간장', '멸치액젓', '다진마늘'],['김치전', '김치', '양파', '대파', '사골육수', '새우젓', '고춧가루', '간장', '다진마늘'],['물', '애호박', '양파', '청양고추', '새우젓', '고춧가루', '미원', '다진마늘', '소금', '후추', '파'],['김치', '스팸', '파', '양파', '청양고추', '다진마늘', '소금', '고춧가루'],['오징어', '양파', '당근', '호박', '무', '청양고추', '고춧가루', '마늘', '식용유', '소금', ''],['콩나물', '두부', '돼지고기', '대파', '청양고추', '청양고추', '고춧가루', '멸치액젓', '다진마늘', '들깨'],['바지락', '양파', '애호박', '두부', '대파', '페페론치노', '계란', '순두부', '물', '참기름', '고춧가루', '소금', '다진마늘', '미원'],['무', '팽이버섯', '양파', '우렁', '청양고추', '두부', '된장', '된장', '고춧가루', '다시다 육수', ''],['당면', '간장', '소고기', '양파', '당근', '버섯', '참깨', '고구마줄기'],['돼지고기', '양파', '파', '양배추', '고추장', '고춧가루', '간장', '설탕', '맛술', '후추'],['오징어', '양파', '다진마늘', '간장', '굴소스', '올리고당', '고춧가루', '깨', '매실액', '참기름'],['갈치', '감자', '양파', '대파', '청양고추', '청양고추', '맛술', '소금', '물', '멸치', '다시마', '건새우', '고춧가루', '간장', '설탕', '맛술', '다진마늘', '생강', '후추'],['소고기', '양파', '당근', '쪽파', '당면', '간장', '올리고당', '맛술', '매실액', '참기름', '후추'],['브로콜리', '파프리카', '양파', '돼지고기', '고추', '마늘', '스리라차소스', '생간', '간장', '녹말가루', '참기름', '후추'],['돼지고기', '간장', '간장', '맛술', '설탕', '생강', '다진마늘', '배', '양파', '참기름', '후추', '물', '대파', '감자', '무', '당근', '인삼', '대추', '표고버섯'],['닭고기', '다진마늘', '소금', '후추'],['돼지고기', '양파', '팽이버섯', '느타리버섯', '간장', '다진마늘', '매실청', '후추', '꿀', '참기름'],['미더덕', '조개', '소고기', '표고버섯', '쌀', '청양고추', '느타리버섯', '콩나물', '미나리', '표고버섯', '간장', '다진마늘', '후추', '소금', '참기름', '간장', '대파', '다진마늘', '소금', '참기름', '대파', '다진마늘', '소금', '소금', '참기름', '간장', '대파', '다진마늘', '소금', '참기름', '간장', '후추', '참기름'],['골뱅이', '미나리', '양파', '사과', '진미채', '참기름', '소금', '소면', '참기름', '간장', '고추장', '설탕', '고춧가루', '다진마늘', '식초'],['닭고기', '고구마', '대파', '모짜렐라치즈', '당면', '다진마늘', '고춧가루', '올리고당', '개복숭아', '간장', '맛술', '카레', '설탕'],['순대', '양배추', '양파', '대파', '청양고추', '쫄면', '당면', '참기름', '깨', '깻잎', '간장', '다진마늘', '고추장', '설탕', '후추', '고춧가루', '들깨', '물'],['떡갈비', '샐러드야채'],['탕수육소스', '돼지고기', '식용유', '전분', '당근', '양파', '목이버섯', '오이', '물'],['두부', '대파', '파프리카', '다진마늘', '양파', '쪽파', '된장', '고추장', '고춧가루', '찹쌀', '참기름', '굴소스', '소고기', '물', '후추'],['돼지고기', '바베큐소스', '스테이크소스', '식용유', '양파', '피망', '피망', '고추', '청양고추', '물'],['크래미', '크림치즈', '라이스페이퍼', '올리브유'],['새우', '허브맛솔트', '마늘', '고춧가루', '올리브유'],['돼지고기', '양파', '깻잎', '대파', '팽이버섯', '고추장', '고춧가루', '다진마늘', '간장', '올리고당', '매실청', '굴소스', '참기름', '생강', '후추'],['닭고기', '감자', '표고버섯', '당면', '청양고추', '물', '간장', '설탕', '마늘', '생강', '대파', '맛술', '참기름', '소금'],['김치전', '김치', '부침가루', '물', '계란', '김치', '두부', '두부', '김치', '양파', '들기름', '올리고당'],['주꾸미', '밀가루', '당근', '양파', '청양고추', '대파', '고춧가루', '고추장', '간장', '물엿', '다진마늘', '생강', '매실액', '후추', '참기름', '참깨'],['낙지', '대파', '양파', '당근', '양배추', '청양고추', '청양고추', '밀가루', '소금', '고추장', '고춧가루', '다진마늘', '미원', '매실청', '설탕', '간장', '참기름', '후추', '참깨'],['소고기', '대추', '사과', '무', '당근', '간장', '후추', '매실액'],['코다리', '무', '양파', '청양고추', '파', '사골육수', '고추장', '고춧가루', '간장', '맛술', '물엿', '설탕', '다진마늘', '생강'],['밀가루', '찹쌀', '고추장', '된장', '고춧가루', '물', '깻잎', '부추', '고추', '청양고추'],['냉동꽃빵', '돼지고기', '양파', '당근채', '캔죽순', '피망', '피망', '표고버섯', '마늘', '배트남고추', '식용유', '고추기름', '백후추', '간장약', '굴소스약', '설탕또는미원'],['밀가루', '스파게티소스', '모짜렐라치즈', '양파', '토마토', '햄', '양송이버섯', '피망', '올리브'],['라자냐', '소고기', '양파', '시금치', '아스파라거스', '생크림', '토마토', '리코타치즈', '파마산치즈', '빵가루', '바질', '스파게티소스', '올리브유', '소금', '후추', '완두콩', '새싹'],['또띠아', '양파', '당근', '옥수수콘', '올리고당', '마요네즈', '후추', '모짜렐라치즈'],['떡볶이떡', '간장', '고추장', '고춧가루', '설탕', '물'],['감자', '양파', '닭고기', '스팸', '시금치', '피망', '모짜렐라치즈', '치즈', '콩', '밀가루', '스파게티소스'],['치즈', '또띠아', '계란', '', '', '깻잎', '설탕', '버터'],['닭고기', '양파', '양배추', '계란', '아보카도', '해바라기씨', '아몬드', '단호박', '소금', '후추', '올리브유', '올리고당'],['감자', '부침가루', '부추', '당근', '소금'],['라자냐', '양파', '양송이버섯', '당근', '단호박', '스파게티소스', '버터', '밀가루', '모짜렐라치즈'],['햇반', '양파', '양파', '방울토마토', '가지', '애호박', '돼지고기', '소고기', '물', '스파게티소스', '올리브유', '소금', '바질'],['애호박', '양파', '당근', '파프리카', '햄', '햇반', '버섯', '굴소스', '미원'],['가지', '베이컨', '양파', '방울토마토', '모짜렐라치즈', '스파게티소스'],['밀가루', '계란', '김치', '물'],['레시피마다달라요!'],['햇반', '치즈', '계란', '양파', '쪽파', '버터', '마요네즈', '스리라차소스'],['부침가루', '베이컨', '마요네즈', '양배추'],['콘치즈', '버터', '양파', '청양고추', '마요네즈', '모짜렐라치즈', '칵테일새우', '후추'],['닭고기', '전분', '식용유', '대파', '소금', '후추', '맛술', '간장', '레몬즙', '식초', '설탕', '고추', '청양고추'],['감자', '찹쌀', '치즈', '물', '식용유', '소금'],['소고기', '아스파라거스', '파프리카', '소시지', '마늘', '올리브유', '버터', '후추', '소금'],['치즈볼', '호떡'],['카레', '감자', '당근', '양파', '브로콜리', '사과', '우유', '완두콩'],['또띠아', '모짜렐라치즈', '체다치즈', '스파게티소스', '연어캔', '샐러드야채', '바나나'],['당근', '부추', '양파', '느타리버섯', '감자', '옥수수', '햇반', '돼지고기', '간장', '다진마늘', '참기름', '올리고당', '케첩', '모짜렐라치즈', '소금', '후추'],['돼지고기', '햄버거번', '양상추', '양파', '슬라이스치즈', '토마토', '돈까스소스', '마요네즈', '스위트칠리소스', '식용유', '피클', '양배추'],['소고기', '양파', '피망', '당근', '버섯', '버터', '맛술', '소금', '후추', '스테이크소스', '굴소스', '케첩', '올리고당', '다진마늘'],['계란', '토마토', '스트링치즈', '양배추', '크래미', '양파', '소금', '후추'],['소고기', '김치', '스파게티소스', '모짜렐라치즈', '파슬리'],['베이컨', '계란', '소시지', '옥수수콘', '우유', '감자', '양파', '치즈'],['연어', '새싹', '비트', '마늘', '소금', '후추', '비트', '오렌지주스', '포도씨유', '소금'],['새우', '마늘', '페페론치노', '올리브유', '포도씨유', '소금', '후추', '다진마늘', '바게트빵', '로즈마리'],['계란', '우유', '버터', '후추', '소금', '파슬리'],['마늘', '냉동칵테일새우', '페페론치노', '브로콜리', '식빵', '소금', '후추', '로즈마리'],['스파게티소스', '3분 미트볼', '베이컨', '계란', '바질', '양파', '모짜렐라치즈', '방울토마토', '후추', '바게트빵'],['감자', '새우', '양파', '파프리카', '가지', '토마토', '버터', '파마산치즈', '소금', '후추'],['소고기', '양송이버섯', '아스파라거스', '가지', '파프리카', '양파', '고구마', '감자'],['라면', '스프', '토마토', '애호박', '가지', '새송이버섯', '양파', '스파게티소스', '마늘', '파프리카', '올리브유'],['마카로니', '물', '체다치즈', '후추'],['바게트빵', '크래커', '떡볶이떡', '치즈', '포도주', '레몬', '마늘', '녹말가루'],['계란', '우유', '파마산치즈', '소금', '올리브유', '시금치', '양파', '소시지', '양송이버섯', '토마토', '모짜렐라치즈'],['소고기', '양배추', '느타리버섯', '소금', '후추', '포도주', '간장', '매실액'],['라면', '라면', '양파', '계란', '우유', '다시마', '멸치', '', '고추장', '물엿', '소금', '케첩', '간장'],['닭고기', '양파', '소금', '후추'],['만두', '양파', '올리브', '모짜렐라치즈', '견과류', '파슬리', '스파게티소스'],['토마토', '마늘', '올리브유', '바질', '양파', '바게트빵', '설탕', '식초', '소금', '파슬리', '후추'],['계란', '체다치즈', '버터', '새싹', '우유', '소금', '후추', '토마토', '양파', '올리브유', '케첩', '핫소스', '설탕', '식초', '파슬리', '레몬즙', '소금', '후추']]
# value = [['', '', ''],['1개', '조금', '1개'],['2큰술', '1/4개', '50g', '조금', '100g', '1큰술', '1큰술', '1큰술', '1큰술', '약간', '1/4개', '1/4개', '2큰술', '2큰술', '1큰술', '2큰술', '4큰술', '8큰술', '3큰술', '3큰술', '1큰술', '1큰술'],['400g'],['', '', '', '', '', ''],['', '', '', '', '', '', '', '', '', ''],['1인분', '2공기', '1/3개', '', '약간'],['100g', '1개', '1/4개', '1개', '', '', '1숟가락', '4컵', '', '약간'],['400g', '1/2개', '1/2개', '1/2개', '100원짜리 만큼', '1/2대', '8컵', '2스푼', '1스푼', '조금', '1/3스푼~1/2스푼'],['200g', '30g', '0.5T', '1T', '2T', '0.5T'],['', '조금', '조금', '', ''],['3종이컵', '0.5큰술', '5인분', '1/2개', '1개'],['100g', '1장', '1/2개', '조금', '1개', '2개', '1t', '톡톡', '톡톡', '1t', '1t', '1t'],['1개', '1장', '1줌', '2포기', '약간', '1/2대', '3T'],['1줌', '1줌', '1줌', '1개', '1/2줌', '1/2티스푼', '1+1/2티스푼', '1장', '1줌', '8부(그릇)', '8부(그릇)', '1티스푼', '1티스푼', '약간'],['1개', '1개', '1개', '적당량', '1큰술', ''],['3개', '1개'],['1/2포기', '500원 동전보다 살짝 크게 움켜쥔 정도(', '0.5스푼', '1.5스푼', '1스푼', '0.5스푼', '1.5스푼', '0.5스푼', '2티스푼'],['', '', '', '', '', ''],['1/2병', '2인분', '1/4개', '2~3조각', '3개', '2장', '5개'],['1/4쪽', '조금', '약간', '1/4쪽', '', '', '', '', '', '', '', '', '', '', ''],['2인분', '1개', '100g', '', '약간', '약간'],['', '', '', '', '', '', '', ''],['', '', '', '', '', '', '', '', ''],['3개', '1/2쪽', '5개', '1/2개', '3쪽', '3큰스푼', '1티스푼', '1꼬집'],['2봉지', '넉넉히', '1주먹', '2개'],['200g', '350ml', '250g', '2줌', '1개', '', '', '1.5큰 술', '계량'],['1인분분량', '1/2개', '1/2개', '7마리', '2컵', '2t', '조금', ''],['1인분(500원크기)', '3개', '10개', '약간', '약간', '2~3꼬집', '1/4큰술', '1국자'],['150g', '200g', '3공기', '1조각', '1.5큰술', '1/2작은술', '1작은술', '1작은술', '조금'],['1인분', '1/2컵', '1개'],['', '1줌', '1T', '솔솔', '2인분', '약간'],['', '', '', '', '', ''],['500g 한봉지', '11컵', '2큰술', '1대', '1/2큰술', '2개', '약간', ''],['10마리', '1도막', '2개', '1줌', '1/2개', '2장', '1개', '적당량', '2T', '1/T'],['떡', '멸치육수', '', '', '', ''],['', '1개', '', '', ''],['', '', '', '', ''],['2개', '1/2대', '500ml'],['200g', '1600ml', '2줌', '1줌', '2대', '1토막', '4숟가락', '3숟가락', '1숟가락', '1숟가락', '약간', '약간'],['', '', '', '', '', '', ''],['5개', '1개', '적당량', '500ml', '1/2큰술'],['160g', '3~4개', '500g', '3/4컵', '1t', '1개', '약간'],['전부', '5~6장', '1개', '1개'],['700g', '1/2개', '2뿌리', '1개', '2개', '300g', '2.4L', '4큰술', '2큰술', '1큰술', '1큰술', '1큰술', '2큰술', '1작은술', '1꼬집'],['2줌', '1/2모', '1줌', '약간', '약간', '4~5컵', '1.5스푼'],['100g', '1/4개', '1뿌리', '1개', '1/2개', '1모', '1L', '4큰술', '1큰술', '1큰술', '1꼬집'],['2개', '1/2개', '2개', '2개', '2T', '1T', '2T', '2T', '4T', '1/4종이컵', '1.5T', '1L'],['', '', '', '', '', '', '', '', ''],['1개', '1/3개', '1/2개', '', '1T', '', '', ''],['1250g', '37g', '10개', '약간', '1개', '3L', '약간', '약간', '1/2T'],['1컵', '1컵', '1개', '조금', '1/2대', '1T', '8컵', '2개', '1T', '', '약간', '1T'],['1kg', '4개', '6장', '1묶음', '1/2단', '1/2개', '3개', '1큰술', '4큰술', '1+1/2큰술', '1/2컵', '1큰술', '3큰술', '5쪽', '1톨', '10알'],['1팩(60-70개)', '1500ml', '1큰술', '1대', '2개', '3/2큰술'],['', '', '', '', '', '', '', '', '', '', '', ''],['1/2봉', '2/3포기', '1스푼', '1개'],['80g', '1/2뼘', '3큰술', '1t', '1큰술', '1큰술', '1모', '2개', '1줌', '3큰술', '1큰술'],['2컵', '1/6개', '1/2개', '1대', '1개', '1/2작은술', '1큰술'],['', '', '', '', '', '', '', '', '', ''],['1주먹', '1주먹', '1개', '4조각', '1/4', '1/2뿌리', '1/4모', '1.5T', '1T', '1t', '1t'],['200g', '1/4쪽', '2컵', '약간', '약간'],['1팩', '1/2개', '1/2대', '1개', '2컵(약 400ml 정도)', '1큰 술', '2큰 술', '1큰 술', '2큰 술', '4큰 술', '1큰 술', '1큰 술', '적당량'],['1', '1', '1', '1/4개', '1/2개', '1/4개', '1/2', '1'],['200g', '1/2개', '1개', '1/2모', '200g', '50g', '2T', '2T', '1T', '조금', '조금'],['1개', '1개', '1/2개', '1/2개', '1/2모', '1/3개', '1.5컵', '약간', '2개', '4컵', '', '1큰술', '2국자', '2큰술', '1큰술'],['1/4포기', '190g', '2/3개', '1개', '1개', '1T', '1T', '1T', '1T', '적당량', '600ml'],['300g', '1/2개', '1대', '1개', '적당히', '1t', '조금', '1T'],['1모', '조금', '조금', '1뿌리', '2조각', '1T', '조금', '1T', '4T'],['2마리', '1/4모', '1줌', '1줌', '1줌', '2대', '10개', '3개', '2개', '5큰술', '2큰술', '1큰술', '2+1/2큰술', '1큰술반', '3큰술', '', '2장', '3개', '10개', '2큰술', '1/2개', '1/2개', '3개', '1대', '1800ml'],['200g', '1/2개', '1/4개', '1개', '1개', '1/2개', '2개', '1/2모', '4컵', '4큰술', '1큰술'],['작은거', '3개', '1개', '1개', '적당히', '2종이컵', '1/3T', '3T', '1T', '2T', '1T', '1T', '1T'],['100g', '2큰술', '약간', '1/2개', '약간', '1개', '1/2개', '3뿌리', '', '1/2큰술', '2작은술', '1큰술', '1큰술', '약간'],['450g', '', '1/6쪽', '1/2컵', '250cc', '1T', '조금', '1t', '1/2개', '1개', '1/3개', '1대', '2개', '1개', '1t', '1T \u200b'],['2컵', '1캔', '1/2개', '1개', '1개', '1/2모', '1큰술', '약간'],['300g', '1개', '1/2개', '1/2개', '1개', '1개', '', '1T', '1T', '1.5T', '1T', '약간', '1장', '10-12마리'],['200g', '100g', '100g', '1개', '1개', '3T', '1T', '0.5T', '2T', '1T'],['1/3개', '1/2개', '1/2모', '', '', ''],['', '', '', '', '', '', '', '', '', '', '', ''],['4개', '100g', '100g', '1/2개', '1개', '1개', '600ml', '2T', '2T', '1T', '1T', '1T', '1T', '1T'],['12~15개 정도', '1줌', '1개', '1/2대', '500ml', '1/2~1숟가락', '1숟가락', '1숟가락', '1숟가락'],['2머그컵', '1/2개', '1/2쪽', '2개', '1/2숟가락', '1/2숟가락', '1/2숟가락', '1/2숟가락', '조금', '조금', '조금'],['', '', '', '', '', '1큰술', '', '1큰술'],['2마리', '1개', '1/2개', '1/3개', '조금', '2개', '2숟가락', '1/2숟가락', '조금', '조금', '자박하게'],['1봉지(300g)', '1모', '120g', '2대', '1개', '1개', '5큰술', '3~4큰술', '1큰술', '4큰술'],['3줌', '1/2개', '1/3개', '1/2모', '1뿌리', '1봉', '4개', '400g', '2L', '1큰술', '4큰술', '1큰술', '1큰술', '1/2작은술'],['', '', '1/2개', '1줌', '1개', '1/2모', '1', '1/2', '약간', '1', ''],['', '', '', '', '', '', '', ''],['500~600g', '1개', '2줌', '100g', '3~4T', '2T', '2T', '1.5T', '1T', '톡톡'],['3마리', '1/4개', '1/3T', '2T', '1T', '2T', '1/3T', '0.5T', '1T', '0.5T'],['5토막(1마리)', '2개', '1개', '1대', '1개', '1개', '1큰술', '1꼬집', '5컵', '10마리', '1장(6x6)', '1줌', '3큰술', '4큰술', '1큰술', '2큰술', '1큰술', '1큰술', '약간'],['550g', '', '', '', '1T', '6T', '1T', '2T', '2T', '2T', ''],['50g', '1개', '1개', '300그램', '3개', '4쪽', '3큰술', '', '3큰술(없으면 맛간장으로)', '2큰술', '1/2큰술', '약간'],['5kg', '2컵', '1/2컵', '1컵', '1컵', '1수저', '1/2컵', '1개', '3개', '5수저', '1/2수저', '3컵', '2~3컵', '1개', '1토막', '1토막', '조금', '3알', '2장'],['500g', '10g', '약간', '약간'],['330g', '', '', '', '', '', '', '', '', ''],['', '', '', '', '4스푼', '2개', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],['400g', '1줌', '1/2개', '1/4개', '1컵', '2T', '왕창', '500원동전크기', '1T', '1T', '2T', '4T', '4T', '2T', '10T'],['1.5kg', '200g', '100g', '300g', '100g', '1/4cup', '1/3cup', '1/4cup', '1/4cup', '1/3cup', '1/4cup', '1tbsp', '1tbsp'],['1줄', '1/4통', '1/2개', '1대', '3-4개', '1인분', '1인분', '1/2큰술', '약간', '3~4장', '2큰술', '1큰술', '1큰술', '1작은술', '약간', '2작은술', '4큰술', '50ml'],['', ''],['1 봉', '300 g', ' 약간', '100 g', '1/4 개', '1/3 개', '2 장', '1/4 개', '1/2 컵'],['1모', '', '', '', '', '', '', '', '', '', '', '1T', '100g', '2스푼', '약간'],['2인분', '4큰술', '4큰술', '약간', '1/2개', '1/2개', '1/2개', '1/2개', '1/2개', '150ml'],['7개', '3', '7', '적당히'],['8마리', '약간', '1작은술', '1/4작은술', '2~3큰술'],['1근', '1개', '6장', '', '', '1T', '3T', '1T', '2T', '1T', '1T', '1T', '1T', '', ''],['125g', '100g', '2개', '30g', '약간', '100ml', '3T', '2.5T', '1t', '0.5t', '2줌', '1T', '1T', '1꼬집'],['', '1포기', '', '', '1개', '1국자', '', '1개', '1포기', '1/2개', '1T', '1T'],['7마리', '1+1/2큰술', '1/2개', '1/2개', '1개', '1/2대', '2큰술', '1큰술', '2큰술', '2큰술', '1작은술', '1큰술', '2큰술', '1g', '1작은술', '조금'],['3마리', '1대', '1개', '1/5개', '1/6개', '2개', '1개', '2큰술', '1/2큰술', '1큰술', '4큰술', '1큰술', '1큰술', '1큰술', '1큰술', '2큰술', '1큰술', '적량', '적량'],['1kg', '10개', '1개', '1/3', '1개', '5t', '약간', '1t'],['1kg', '1/10개', '1개', '3개', '약간', '400ml', '1T', '2T', '5T', '3T', '3T', '1T', '2T', '조금'],['1컵', '3스푼', '2스푼', '1스푼', '1작은스푼', '1컵', '10장', '1/4줌', '1/2개', '1/2개'],['4개', '1/2근', '1+1/2개', '1/2개', '1개', '1~1.5개', '1~1.5개', '4개', '6개', '4~6개', '2T', '2~4T', '약간', '2T', '2T', '2T'],['', '', '', '', '', '', '', '', ''],['4 장', '20 g', '1 개', '20 g', '4 대', '100 ㎖', '1 개', '100 g', '50 g', '30 g', '5 g', '1/2 병', ' 적당량', ' 약간', ' 약간', '30g', '약간'],['1장', '1/3개', '1/5개', '1컵', '', '', '약간', '약간'],['2인분', '2스푼', '1스푼', '1스푼', '2스푼', '2컵'],['8개', '1개', '1덩어리', '1/2개', '적당량', '적당량', '적당량', '2장', '적당량', '3컵', '5T'],['1개', '1개', '1개', '1개', '', '적당양', '적당량', '조금'],['100g', '1/2개', '조금', '1개', '1/2개', '조금', '조금', '1/2개', '약간', '약간', '닭가슴살이코팅될정도', '약간'],['4개', '2스픈', '1줌', '', ''],['6장', '1/2개', '1주먹', '1/2개', '1/4개', '250g', '20g', '1T', '200g'],['1 개', '30 g', '30 g', '3 개', '1/4 개', '1/6 개', '30 g', '30 g', '150 g', '240 g', ' 적당량', ' 약간', '약간'],['', '', '', '', '', '', '', '2큰술', '1큰술'],['1개', '100g', '1/2개', '10개', '50g', '5스푼'],['1컵', '1개', '1줌', '적당량'],[''],['2개', '2장', '3개', '1개', '2줄', '', '2T', '1T'],['1박스', '3줄', '약간', '1/8통'],['1/2캔', '20g', '1/2개', '2~3개', '넉넉히', '넉넉히', '1줌', '약간'],['500g', '1컵', '적당량', '3~4뿌리', '1/2작은술', '약간', '3큰술', '2큰술', '1.5큰술', '1큰술', '1큰술', '1개', '1개'],['5개', '4큰술', '2장', '', '', '약간'],['2덩어리', '4개', '1/2개', '12조각', '4개', '듬뿍', '4조각', '4꼬집', '4꼬집'],['', ''],['', '', '', '', '', '', '', ''],['', '', '', '', '', '', ''],['15g', '2Ts', '30g', '30g', '1/2개', '3Ts', '1공기', '50g', '1/4ts', '1/4ts', '1/4ts', '약간', '약간', '약간', '약간', '약간'],['1개', '2개', '3장', '1/4개', '2장', '1/4개', '1/2봉', '2큰술', '2큰술', '적당량', '4개', '2장'],['300g', '1/2개', '1/2개', '1개', '3개', '약간', '1큰술', '약간', '약간', '4큰술', '2큰술', '1큰술', '2큰술', '1큰술'],['2알', '1/2개', '1개', '1주먹', '1개', '기호에따라', '1티스푼', '약간'],['4개', '150g', '100g', '4장', '조금'],['5장', '2개', '1개', '1캔', '200ml', '1개', '1/2개', '1개'],['220g', '40g', '1개', '5개', '약간', '약간', '4T', '4T', '1T', '약간'],['20마리', '7알', '10알', '1/2종이컵', '1/4종이컵', '약간', '약간', '1/2숟가락', '2~4조각', '1줄'],['4알', '50ml', '소량', '1꼬집', '1꼬집', ''],['10톨', '20마리', '4개', '1/4개', '먹을만큼', '1티스푼', '조금', '조금'],['3~4컵', '', '3줄', '2개', '줌', '1개', '100g', '7~8개', '약간', '3~5개'],['2개', '1줌', '', '', '', '2개', '', '', '', ''],['2덩어리', '', '', '', '', '', '', ''],['70g', '8g', '230g', '30g', '25g', '25g', '150g', '90g', '30g', '40g', '5g'],['1봉지', '150ml', '1장', '2인분)'],['', '', '', '400g', '1컵', '1/2개', '1개', '1작은술'],['5개', '150ml', '2큰 술', '1작은술', '조금', '1줌', '1/2개', '1개', '1컵', '1줌', '1줌'],['150g', '', '약간', '약간', '약간', '3숟가락', '2숟가락', '2숟가락'],['1봉', '1/2개', '20g', '4ea', '1/2C', '1ea', '4ea', '', '1Ts', '4Ts', '2Ts', '1Ts', '1Ts'],['1개', '1/2개', '약간', '약간'],['5개', '1/4개', '1큰술', '적당량', '약간', '약간', '4큰술'],['2개', '', '1T', '20g', '1/2개', '1', '1/2작은술', '1/2직은술', '1꼬집', '약간', '약간'],['3개', '1큰술', '1큰술', '1줌', '2큰술', '약간', '약간', '1/3개', '1/4개', '2큰술', '2큰술', '1/2큰술', '1/2큰술', '1/2큰술', '약간', '약간(생략가능)', '약간', '약간']]
#
# unit_dict = dict()
#
# for i in range(len(key)):
#     for j in range(len(key[i])):
#         if key[i][j] in unit_dict:
#             unit_dict[key[i][j]].append(value[i][j])
#         else:
#             unit_dict[key[i][j]] = [value[i][j]]
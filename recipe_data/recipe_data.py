import json, pandas as pd

# 크롤링 데이터 불러오기

with open('./recipe_data/recipe_table.json', 'rt', encoding='UTF8') as f:
    rc = json.loads(f.read())

df_rc = pd.DataFrame(rc)

# 중복 메뉴 정리 -
df_rc = df_rc.drop_duplicates(['RECIPE_NM'], keep='first', ignore_index=True)

# 재료 없음 정리 - 인덱스 그대로
ingd_null = df_rc['INGREDIENTS'].isin([[]])
df_rc = df_rc[~ingd_null]

# 레시피 없음 정리 : df_rc 153개, df_igd 160개
recipe_null = df_rc['RECIPE'].isin([[]])
df_rc = df_rc[~recipe_null]

# 레시피 재료 표준 딕셔너리
key = ["우동","우동소스","오뚜기(3분미트볼)","혼다시","가지","간장","국간장","만능간장","양조간장","조림간장","진간장","집간장","갈치","감자","감자(中)","감자小","감자작은거","감자중","감자큰사이즈","개복숭아","건새우","새우가루","견과류","견과류가루","계란","계란노른자","달걀","고구마","고구마줄기","고사리","불린고사리","고추","아삭이고추","청고추","풋고추","고추장","고추장찌개","고운고춧가루","고추가루","고춧가루","굵은고춧가루","골뱅이","굴소스","김","김가루","김볶음","김장김치","김치","김치국물","김치양손","김치찌개","김칫국물","묵은김치","배추김치","신김치","김치부침개","모듬전","깨","깻잎","꽁치통조림","손질꽃게","꿀","낙지","냉동꽃게","냉동새우","냉동칵테일새우","녹말가루","녹말물","느라티버섯","느타리버섯","맛타리버섯","다시다","다시육수","디포리육수혹은","멸치다시육수","멸치육수","액상조미료","요리에한수","육수티백","한방팩","다시마","다시마5cmx5cm","다진마늘","단호박","닭","닭가슴살","닭갈비","닭고기","닭다리살","닭볶음탕","삼계탕용생닭","당근","당근채손으로","납작당면","당면","당면사리","당면설탕","잡채","대추","밤대추","굵은파","다진파","대파","설어놓은대파","파채","카츠야로스까스동봉소스","동태","다진돼지고기","대패삼겹살","돈까스","돼지갈비","돼지고기","돼지고기간것","돼지고기다짐육","돼지고기등심","돼지고기앞다리","불고기","수육","카츠야로스까스","돼지뼈","된장","미소된장","시판된장","집된장","된장국","더프레시안행복한콩브런치두부감자","두부","두부김치","두부반모","포프리두부","들기름","들깨가루","들깻가루","떡갈비","떡","떡국","오뚜기우리쌀떡국떡","떡볶이","떡볶이떡","또띠아","또띠아피자","라면","라면사리","라면스프","삼양라면","신라면","진짜진짜(면)","라자냐","레몬","레몬즙","로즈마리","리코타치즈","간마늘","두쪽마늘다진것","마늘","마늘가루","통마늘","편마늘","편썬마늘","마요네즈","맥앤치즈","만두","오뚜기옛날왕만두","맛술","생강술","청주","매실액","매실엑기스","매실원액","매실청","멸치","멸치액젓","액젓","모짜렐라치즈","슬라이스모짜렐라치즈","피자치즈","목이버섯","무","무3cm","무우","채썬무","뜨거운물","물","생수","물엿","미나리","만데기","건미역","미역국","미림","미원","미향","소고기다시다","연두순","요리당","천연조미료","밀가루","피자도우","구운빵","바게트빵","치아바타(바게트)","바나나","바베큐소스(매운맛)","바지락","생바지락크게","바질","바질한","신선한바질잎","방울토마토","다진배","배","배추","배추잎","속배추","흰콩(백태)불린것","버섯","버터","베이컨","부추","부침가루","오코노미야끼","북어","브로콜리","비빔면","구운비트간것","비트","빵가루","사골육수","오뚜기옛날사골곰탕국물","육수","사과","사과배양파","상추","새송이버섯","어린잎채소","새우","중하","중하새우","새우젓","샐러드야채","비타민야채","샐러리","생간","다진생강","생강","생강가루","생강즙","통구맹이","생크림","휘핑크림","검은콩(서리태)","설탕","원당","국거리소고기","등심스테이크","소갈비","소고기","소고기다짐육","소고기샤브샤브","소고기양지머리","소고기차돌박이","소불고기","쇠고기","쇠고기다진것","스테이크","안심스테이크","양지","프로슈토","함박스테이크","굵은소금","깨소금","꽃소금","소금","소금(입맛에맞게)","소금반","천일염","국수","소면","잔치국수","소시지","소주","수제비","숙주","숙주나물","숙주크게","순대","순두부","스리라차소스","스리랏차","스위트칠리소스","스테이크소스","스트링치즈","백설토마토파스타소스","스파게티소스","시판용토마토소스","시판크림스파게티소스","오뚜기프레스코스파게티소스토마토","크림소스","토마토소스","토마토파스타소스","토마토파스타소스(약225g)","스팸","스팸큰사이즈","진짜진짜(스프)","슬라이스고다치즈","시금치","식빵","식용유","요리유","튀김용기름","식초","쌀","쌀국수","월남쌈","쑥갓","슬라이스아몬드","아보카도","아보카도오일","아스파라거스","애호박","양배추","양배추채썰어서","적양패주","적채","양상추","양송이","양송이버섯","다진양파","양파","양파작은거","적양파","사각어묵","어묵","연어","연어캔","오렌지껍질","오렌지주스","오이","물오징어","오징어","옥수수","옥수수콘","올리고당","블랙올리브슬라이스","올리브","엑스트라버진올리브오일","올리브오일","올리브유","완두콩","우거지","우동면","우렁","우유","유자폰즈소스","인삼","감자전분","전분","조개살","주꾸미","진미채","짜장면","짬뽕","쪽파","쫄면","쫄면사리","참기름","창참기름","참깨","통깨","참깨흑임자드레싱","참치액","참치액젖","참치","참치캔기름","캔참치","찹쌀","찹쌀가루","청경채","청국장","매운고추","붉은고추","청량고추","청양고추","청양초","청홍고추","홍고추","체다슬라이즈치즈","체다치즈","체더슬라이스","슬라이스치즈","치즈","치킨스톡","카레","카레가루","칵테일새우","칼국수","케찹","케첩","냉동코다리","콘치즈","콩가루","콩나물","비지","크래미","크래커","크림치즈","백설탕수소스","잘익은토마토","토마토","파","치즈가루","파마산치즈","파마산치즈가루","스파게티","스파게티면","스파게티면손가락","파스타","파스타면","파슬리","파슬리가루","파프리카","팽이버섯","팽이버섯작은것","페퍼론치노","페페로치노","페페론치노","포도씨유","레드와인","백포도주","화이트와인","불린표고버섯","생표고보섯","표고버섯","붉은피망","청피망","피망","피망&파프리카","홍피망","오이피클","한약재료","핫바","핫소스","해바라기씨","더프레시안건강한브런치후랑크리치치즈","햄","햄버거번","햄버거번or모닝롤","밥","밥숟가락","햇반","허브맛솔트","봄내음이호박","쥬키니호박","호박","호박등각종(없음생략)","홍합","홍합탕","황태","황태머리","통후추","통후추약간등(","후추","후추가루","후추소금","후춧가루","훗추가루","흑후추가루","국남은것","국자","담을접시","비닐팩","쌀뜨물","쌀뜬물","원하는재료","큰그릇"]
value = ["우동면","간장","3분 미트볼","가쓰오부시","가지","간장","간장","간장","간장","간장","간장","간장","갈치","감자","감자","감자","감자","감자","감자","개복숭아","건새우","건새우","견과류","견과류","계란","계란","계란","고구마","고구마줄기","고사리","고사리","고추","고추","고추","고추","고추장","고추장","고춧가루","고춧가루","고춧가루","고춧가루","골뱅이","굴소스","김","김","김","김치","김치","김치","김치","김치","김치","김치","김치","김치","김치전","김치전","깨","깻잎","꽁치통조림","꽃게","꿀","낙지","냉동꽃게","냉동새우","냉동칵테일새우","녹말가루","녹말가루","느타리버섯","느타리버섯","느타리버섯","다시다","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시다 육수","다시마","다시마","다진마늘","단호박","닭고기","닭고기","닭고기","닭고기","닭고기","닭고기","닭고기","당근","당근","당면","당면","당면","당면","당면","대추","대추","대파","대파","대파","대파","대파","돈까스소스","동태","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지고기","돼지뼈","된장","된장","된장","된장","된장","두부","두부","두부","두부","두부","들기름","들깨","들깨","떡갈비","떡국떡","떡국떡","떡국떡","떡볶이떡","떡볶이떡","또띠아","또띠아","라면","라면","라면","라면","라면","라면","라자냐","레몬","레몬즙","로즈마리","리코타치즈","마늘","마늘","마늘","마늘","마늘","마늘","마늘","마요네즈","마카로니","만두","만두","맛술","맛술","맛술","매실액","매실액","매실액","매실청","멸치","멸치액젓","멸치액젓","모짜렐라치즈","모짜렐라치즈","모짜렐라치즈","목이버섯","무","무","무","신","물","물","물","물엿","미나리","미더덕","미역","미역","미원","미원","미원","미원","미원","미원","미원","밀가루","밀가루","바게트빵","바게트빵","바게트빵","바나나","바베큐소스","바지락","바지락","바질","바질","바질","방울토마토","배","배","배추","배추","배추","백태","버섯","버터","베이컨","부추","부침가루","부침가루","북어","브로콜리","비빔면","비트","비트","빵가루","사골육수","사골육수","사골육수","사과","사과","상추","새송이버섯","새싹","새우","새우","새우","새우젓","샐러드야채","샐러드야채","샐러리","생간","생강","생강","생강","생강","생선","생크림","생크림","서리태","설탕","설탕","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소고기","소금","소금","소금","소금","소금","소금","소금","소면","소면","소면","소시지","소주","수제비","숙주","숙주","숙주","순대","순두부","스리라차소스","스리라차소스","스위트칠리소스","스테이크소스","스트링치즈","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스파게티소스","스팸","스팸","스프","슬라이스치즈","시금치","식빵","식용유","식용유","식용유","식초","쌀","쌀국수","라이스페이퍼","쑥갓","아몬드","아보카도","아보카도오일","아스파라거스","애호박","양배추","양배추","양배추","양배추","양상추","양송이버섯","양송이버섯","양파","양파","양파","양파","어묵","어묵","연어","연어캔","오렌지","오렌지주스","오이","오징어","오징어","옥수수","옥수수콘","올리고당","올리브","올리브","올리브유","올리브유","올리브유","완두콩","우거지","우동면","우렁","우유","유자폰즈소스","인삼","전분","전분","조개","주꾸미","진미채","짜장면","짬뽕","쪽파","쫄면","쫄면","참기름","참기름","참깨","참깨","참깨흑임자드레싱","참치액","참치액","참치캔","참치캔","참치캔","찹쌀","찹쌀","청경채","청국장","청양고추","청양고추","청양고추","청양고추","청양고추","청양고추","청양고추","체다치즈","체다치즈","체다치즈","치즈","치즈","치킨스톡","카레","카레","칵테일새우","칼국수","케첩","케첩","코다리","콘치즈","콩","콩나물","콩비지","크래미","크래커","크림치즈","탕수육소스","토마토","토마토","파","파마산치즈","파마산치즈","파마산치즈","파스타면","파스타면","파스타면","파스타면","파스타면","파슬리","파슬리","파프리카","팽이버섯","페페론치노","페페론치노","페페론치노","페페론치노","포도씨유","포도주","포도주","포도주","표고버섯","표고버섯","표고버섯","피망","피망","피망","피망","피망","피클","한약재료","핫바","핫소스","해바라기씨","햄","햄","햄버거번","햇반","햇반","햇반","햇반","허브맛솔트","호박","호박","호박","호박","홍합","홍합","황태","황태","후추","후추","후추","후추","후추","후추","후추","후추","","","","","","","",""]
std_ingd = dict(zip(key, value))

# 띄어쓰기 없애기, 표준 명칭으로 변경
for ingredient in df_rc['INGREDIENTS']:
    # print(ingredient, type)
    for j in range(len(ingredient)):
        ingredient[j] = ingredient[j].replace(" ", "")
        try:
            ingredient[j] = std_ingd[ingredient[j]]
        except:
            pass
        # 빈 재료에 0 넣기
        if ingredient[j] == '':
            ingredient[j] = 0


# 재료 수량 ''값 처리 : 1
for recipe in df_rc['UNITS']:
    # print(ingredient, type)
    for j in range(len(recipe)):

        if recipe[j] == '':
            recipe[j] = 1

# # 표준 단위
df_rc["UNITS"] = [[1, 1, 1],[1, 0.5, 1],[1, 0.25, 0.0625, 0.5, 100, 1, 1, 0.016, 1, 0.5, 0.25, 0.25, 0.032, 2, 1, 2, 4, 8, 3, 3, 1, 0.2],[400],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[100, 1, 0.25, 1, 1, 1, 1, 4, 1, 0.5],[400, 0.5, 0.5, 0.5, 50, 0.5, 1.44, 2, 1, 0.5, 0.5],[200, 30, 0.5, 1, 2, 0.5],[1, 0.5, 0.5, 1, 1],[3, 0.5, 5, 0.5, 1],[100, 0.0125, 0.5, 0.5, 1, 2, 1, 0.5, 0.5, 0.33, 0.33, 0.33],[1, 1, 1, 2, 0.5, 0.5, 3],[5, 5, 0.2, 1, 0.5, 0.165, 0.495, 1, 1, 1.44, 8, 1, 1, 0.5],[1, 1, 1, 1, 1, 1],[0.5, 1, 0.5, 1.5, 1, 0.5, 1.5, 0.5, 0.66],[1, 1, 1, 1, 1, 1],[0.5, 2, 0.25, 3, 3, 2, 5],[0.25, 0.5, 0.5, 0.25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1],[3, 0.5, 5, 0.5, 3, 3, 0.33, 0.5],[2, 2, 1, 2],[200, 350, 250, 2, 1, 1, 1, 1.5, 1],[1, 0.5, 0.5, 7, 2, 2, 0.5, 1],[1, 3, 10, 0.5, 0.5, 0.5, 0.25, 1],[1, 1, 1, 1, 1],[150, 1, 630, 10, 1.5, 0.5, 1, 1, 0.5],[1, 0.09, 1],[1, 10, 1, 10, 2, 0.5],[1, 1, 1, 1, 1, 1],[500, 2, 2, 1, 0.5, 2, 0.5, 1],[10, 1, 2, 10, 0.5, 20, 1, 1, 2, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[2, 0.5, 500],[200, 1.6, 2, 1, 2, 1, 4, 3, 1, 1, 0.5, 0.5],[1, 1, 1, 1, 1, 1, 1],[5, 1, 1, 500, 0.5],[160, 4, 500, 0.135, 1, 1, 0.5],[1, 6, 1, 1],[700, 0.5, 2, 1, 2, 1, 2.4, 4, 2, 1, 1, 3, 2, 3, 0.5],[20, 0.5, 10, 0.5, 0.5, 0.9, 1.5],[100, 0.25, 1, 1, 0.5, 1, 1, 4, 1, 1, 0.5],[2, 0.5, 2, 2, 2, 1, 2, 2, 4, 3, 1.5, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 0.66, 0.5, 1, 1, 1, 1, 1],[1250, 37, 10, 0.5, 1, 3, 0.5, 0.5, 0.5],[1, 1, 1, 0.5, 0.5, 1, 8, 2, 1, 1, 0.5, 1],[1, 4, 6, 10, 3, 0.5, 3, 3, 4, 1.5, 0.5, 1, 3, 2, 1, 1],[1, 1.5, 1, 1, 2, 1.5],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[175, 0.66, 1, 1],[80, 2, 3, 0.33, 1, 1, 1, 2, 1, 3, 1],[2, 0.16, 0.5, 1, 1, 0.5, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 0.5, 0.25, 0.5, 0.25, 1.5, 1, 1, 1],[200, 0.25, 2, 0.5, 0.5],[1, 0.5, 0.5, 1, 2, 1, 2, 1, 20, 4, 1, 1, 1],[1, 1, 1, 0.25, 0.5, 0.25, 0.5, 1],[200, 0.5, 1, 0.5, 200, 50, 2, 2, 1, 0.5, 0.5],[1, 1, 1, 1, 1, 1, 1],[0.25, 0.5, 0.66, 1, 1, 1, 1, 1, 1, 1, 0.6],[300, 0.5, 1, 1, 0.5, 0.33, 0.5, 1],[1, 0.5, 0.5, 1, 20, 1, 0.5, 1, 4],[2, 0.25, 10, 1, 10, 2, 10, 3, 2, 5, 2, 1, 2.5, 1.5, 9, 1, 2, 3, 10, 2, 0.5, 0.5, 3, 1, 1.8],[200, 0.5, 0.25, 1, 1, 0.5, 2, 0.5, 4, 4, 1],[0.5, 3, 1, 1, 0.5, 0.36, 0.66, 3, 1, 2, 1, 1, 1],[100, 2, 0.5, 0.5, 0.5, 1, 0.5, 3, 1, 0.5, 2, 1, 1, 0.5],[2, 1, 0.5, 1, 1, 0.5, 1, 0.5],[100, 2, 0.5, 4, 1, 2, 1, 3, 1, 2, 2, 2, 1],[200, 100, 100, 1, 1, 3, 1, 1.5, 2, 1],[0.66, 0.5, 0.5, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[4, 100, 100, 0.5, 1, 1, 0.6, 2, 2, 1, 1, 1, 1, 1],[15, 1, 1, 0.5, 500, 1, 1, 1, 1],[0.36, 0.5, 0.5, 2, 0.5, 0.5, 1.5, 0.5, 0.5, 0.5, 0.5],[1, 1, 1, 1, 1, 1, 1, 1],[2, 1, 0.5, 0.5, 1, 1, 10, 0.5, 1.2, 2, 1, 1, 2, 1, 2, 1, 1],[300, 1, 120, 2, 1, 1, 5, 4, 1, 4],[3, 0.5, 0.66, 0.5, 1, 1, 4, 400, 2, 1, 4, 1, 1, 1.5],[1, 1, 0.5, 1, 1, 0.5, 1, 0.5, 0.5, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1],[600, 1, 2, 0.25, 4, 2, 2, 1.5, 1, 0.5],[3, 0.25, 0.66, 2, 1, 2, 0.66, 0.5, 1, 0.5],[1, 2, 1, 1, 1, 1, 1, 0.5, 0.9, 10, 10, 1, 3, 4, 1, 2, 1, 1, 0.5],[550, 1, 1, 1, 10, 6, 1, 2, 2, 2, 1],[1, 1, 1, 300, 3, 4, 3, 1, 3, 2, 0.5, 0.5],[5000, 36, 9, 1, 18, 1, 0.5, 1, 3, 5, 1.5, 0.54, 3, 1, 1, 1, 0.5, 3, 2],[500, 10, 0.5, 0.5],[330, 1, 1, 1, 1, 1, 1, 1, 1, 1],[400, 1, 0.5, 0.25, 1, 2, 2, 1, 1, 1, 2, 4, 4, 2, 10],[1500, 200, 1, 300, 100, 0.25, 8, 3, 0.25, 8, 0.25, 1, 3],[1, 0.25, 0.5, 1, 4, 1, 150, 0.5, 0.5, 4, 2, 1, 1, 1, 0.5, 2, 4, 0.05],[1, 1],[1, 300,  0.5, 100, 0.25 , 0.66 , 2, 0.25 , 0.09],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100, 0.03, 0.5],[400, 4, 4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.15],[7, 3, 7, 1],[8, 0.5, 1, 0.25, 3],[600, 1, 6, 1, 1, 1, 3, 1, 2, 1, 1, 1, 1, 1, 1],[125, 1, 2, 30, 0.5, 0.1, 3, 2.5, 0.3, 0.15, 2, 1, 1, 0.5],[1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1],[7, 1.5, 0.5, 0.5, 1, 0.5, 2, 1, 2, 2, 1, 1, 2, 5, 1, 0.5],[3, 1, 1, 0.2, 0.16, 2, 1, 2, 0.5, 1, 4, 1, 3, 1, 1, 2, 1, 1, 1],[1000, 10, 1, 0.66, 1, 1.5, 0.5, 1],[1, 0.1, 1, 3, 0.5, 400, 1, 2, 5, 3, 3, 1, 2, 0.5],[12, 45, 2, 1, 0.3, 0.18, 10, 0.25, 0.5, 0.5],[1, 1, 1, 1, 1, 1, 1, 1, 1],[4, 20, 1, 20, 4, 100, 1, 100, 50, 30, 5, 0.5, 1, 0.5, 0.5, 30, 0.5],[1, 0.66, 0.2, 12, 1, 1, 0.5, 0.5],[2, 2, 1, 1, 2, 0.36],[1, 1, 1, 1, 1, 1, 1, 0.5],[8, 1, 1, 0.5, 1, 1, 1, 2, 1, 45, 5],[100, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5],[4, 2, 1, 1, 1],[6, 0.5, 1, 0.5, 0.25, 250, 20, 1, 200],[1, 0.1, 0.1, 3, 0.25, 0.16, 30, 30, 0.15, 240, 1, 0.5, 0.5],[1, 1, 1, 1, 1, 1, 1, 2, 3],[1, 100, 0.5, 10, 50, 5],[12, 1, 1, 1],[2, 2, 3, 1, 2, 1, 2, 1],[1, 3, 0.5, 0.125],[0.5, 20, 0.5, 3, 2, 2, 1, 0.5],[500, 1, 1, 4, 0.5, 0.5, 3, 2, 1.5, 1, 1, 1, 1],[5, 60, 2, 1, 1, 0.5],[200, 4, 0.5, 4, 4, 2, 10, 2, 2],[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],[0.075, 1, 0.1, 3, 0.5, 0.225, 1, 50, 0.08, 0.25, 0.08, 0.5, 0.5, 0.5, 0.5, 0.5],[1, 2, 3, 0.25, 2, 0.25, 0.5, 2, 2, 1, 4, 0.2],[300, 0.5, 0.5, 1, 3, 0.5, 1, 0.5, 0.5, 4, 2, 1, 2, 1],[2, 0.5, 1, 1, 1, 1, 0.3, 0.5],[4, 150, 100, 4, 0.5],[5, 2, 1, 1, 200, 1, 0.5, 1],[220, 40, 1, 5, 0.5, 0.5, 4, 4, 1, 0.5],[20, 7, 10, 0.5, 0.25, 0.5, 0.5, 0.5, 4, 1],[4, 50, 0.5, 0.5, 0.5, 1],[3, 1, 1, 6, 1, 3, 2, 2, 3],[4, 1, 3, 2, 1, 1, 100, 8, 0.5, 5],[2, 1, 1, 1, 1, 2, 1, 1, 1, 1],[200, 1, 1, 1, 1, 1, 1, 1],[1, 8, 1, 0.30, 0.25, 0.25, 150, 1, 2, 0.4, 5],[1, 0.150, 1, 2],[1, 1, 1, 4, 1, 0.5, 1, 1],[5, 150, 2, 1, 0.5, 10, 0.5, 1, 1, 1, 1],[150, 1, 0.5, 0.5, 0.5, 3, 2, 2],[1, 0.5, 0.2, 4, 0.5, 10, 4, 1, 1, 4, 2, 1, 1],[1, 0.5, 0.5, 0.5],[5, 0.25, 1, 1, 0.5, 0.5, 4],[2, 1, 1, 20, 0.5, 1, 0.5, 0.15, 0.5, 0.5, 0.5],[3, 1, 15, 1, 30, 0.5, 0.5, 0.66, 0.25, 2, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]]

# csv export
df_rc.to_csv("./recipe_data/df_rc.csv", encoding='utf-8-sig')

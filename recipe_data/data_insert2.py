import csv
import pymysql

db = pymysql.connect(host='50.18.18.112', port=3306, user='mealproject', password='meal1234', db='meal', charset='utf8')
cursor = db.cursor(pymysql.cursors.DictCursor)

# 테이블 생성
create_sql = '''
CREATE TABLE ingredient_price(
    ID INT(200) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    INGREDIENT_NM VARCHAR(20) NOT NULL,
    UNIT VARCHAR(10) NOT NULL,
    PRICE VARCHAR(20) NOT NULL
)
'''
cursor.execute(create_sql)

# 데이터 삽입
insert_sql = '''
INSERT INTO ingredient_price(INGREDIENT_NM, UNIT, PRICE) values (%s, %s, %s)
'''

f = open('standard_price.csv', 'r', encoding='utf-8-sig')
rd = csv.reader(f)

for line in rd:
    cursor.execute(insert_sql, (line[0], line[1], line[2]))

db.commit()
db.close()
f.close()
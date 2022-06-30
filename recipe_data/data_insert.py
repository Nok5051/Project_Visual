import pymysql
import csv

# mysql 연동
conn = pymysql.connect(host='localhost', user='mealproject', password='meal1234', db = 'meal', charset='utf8') 
curs = conn.cursor(pymysql.cursors.DictCursor) 

# 테이블 생성
create_sql = '''
CREATE TABLE recipe_info(
    ID INT(200) NOT NULL AUTO_INCREMENT,
    RECIPE_NM VARCHAR(20) NOT NULL,
    QNT VARCHAR(10) NOT NULL,
    RECIPE VARCHAR(1000) NOT NULL,
    INGREDIENTS VARCHAR(2000) NOT NULL,
    UNITS VARCHAR(1000) NOT NULL,
    CONSTRAINT recipe_info_PK PRIMARY KEY(id)
)
'''
curs.execute(create_sql) 

# 데이터 삽입
insert_sql = '''
INSERT INTO recipe_info(RECIPE_NM, QNT, RECIPE, INGREDIENTS, UNITS) VALUES (%s,%s,%s,%s,%s)
'''

f = open('./recipe_data/df_rc.csv', 'r', encoding='utf-8-sig')
rd = csv.reader(f)

for line in rd:
    curs.execute(insert_sql, (line[0], line[1], line[2], line[3], line[4]))

conn.commit()
conn.close()
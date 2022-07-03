import pymysql
import csv

# mysql 연동
conn = pymysql.connect(host='50.18.18.112', user='mealproject', password='meal1234', db = 'meal', charset='utf8') 
curs = conn.cursor(pymysql.cursors.DictCursor) 

# 테이블 생성
create_sql = '''
CREATE TABLE Recipe(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    RECIPE_NM VARCHAR(20) NOT NULL,
    CATEGORY VARCHAR(10) NOT NULL,
    QNT VARCHAR(10) NOT NULL,
    RECIPE VARCHAR(2000) NOT NULL,
    INGREDIENTS VARCHAR(1000) NOT NULL,
    UNITS VARCHAR(1000) NOT NULL,
    TOTAL_PRICE VARCHAR(2000) NOT NULL
);

'''
curs.execute(create_sql) 

# 데이터 삽입
insert_sql = '''
INSERT INTO Recipe(RECIPE_NM, CATEGORY, QNT, RECIPE, INGREDIENTS, UNITS, TOTAL_PRICE) VALUES (%s,%s,%s,%s,%s,%s,%s);

'''

f = open('./recipe_data/df_rc.csv', 'r', encoding='utf-8-sig')
rd = csv.reader(f)

for line in rd:
    curs.execute(insert_sql, (line[1], line[2], line[3], line[4], line[5], line[6], line[7]))


# 카테고리 테이블
sql = '''

CREATE TABLE Category(
    ID INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CATEGORY VARCHAR(10) NOT NULL
);

'''

category_intertsql = '''
insert into Category(CATEGORY)
select distinct CATEGORY from Recipe
where CATEGORY not in (select CATEGORY from Category);
);
'''

# curs.execute(sql)

conn.commit()
conn.close()
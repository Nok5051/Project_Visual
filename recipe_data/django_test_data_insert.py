import pymysql
import csv

# mysql 연동
conn = pymysql.connect(host='50.18.18.112', user='mealproject', password='meal1234', db = 'meal', charset='utf8') 
curs = conn.cursor(pymysql.cursors.DictCursor) 

# 테이블 생성
create_sql = '''
CREATE TABLE Category(
    ID INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CATEGORY VARCHAR(10) NOT NULL
)
'''
curs.execute(create_sql) 

# 데이터 삽입
insert_sql = '''
INSERT INTO Category(CATEGORY)
SELECT DISTINCT CATEGORY FROM Recipe
WHERE CATEGORY NOT IN (SELECT CATEGORY from Category)
'''
curs.execute(insert_sql) 

conn.commit()
conn.close()
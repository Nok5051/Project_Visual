import pymysql
import pandas as pd
import csv

meal_db = pymysql.connect(
    user='mealproject',
    passwd='meal1234',
    host='50.18.18.112',
    port=3306,
    db='meal',
    charset='utf8'
)

create_sql = '''CREATE TABLE Map_store (
        id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        addr varchar(255),
        storename varchar(255),
        storetype varchar(255),
        callnum varchar(255),
        menu1 varchar(255),
        menu2 varchar(255),
        menu3 varchar(255),
        menu1_price int(11),
        menu2_price int(11),
        menu3_price int(11)
        )
        '''

with meal_db:
    with meal_db.cursor() as cur:
        cur.execute(create_sql)
        meal_db.commit()



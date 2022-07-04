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


sql = "insert into Map_store (storename, storetype, callnum, menu1, menu2, menu3, menu1_price, menu2_price,  \
      menu3_price, addr) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

f = open('data/map_store.csv', 'r', encoding='utf-8')
rd = csv.reader(f)

curs = meal_db.cursor(pymysql.cursors.DictCursor)

for line in rd:
    print(rd)

    curs.execute(sql, (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]))


meal_db.commit()
meal_db.close()
f.close()

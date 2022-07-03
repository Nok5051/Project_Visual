#https://ttoj.github.io/study/db/intro/MySQL-csv-import/

import pymysql
import pandas as pd



meal_db = pymysql.connect(
    user='mealproject',
    passwd='meal1234',
    host='50.18.18.112',
    port=3306,
    db='meal',
    charset='utf8'
)

curs = meal_db.cursor()

sql = "insert into Map_store (storename, storetype, callnum, menu1, menu2, menu3, menu1_price, menu2_price,  \
      menu3_price, addr) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

df = pd.read_csv("data/map_store.csv", encoding='utf-8', engine='python')

for idx in range(len(df)):
    curs.execute(sql, tuple(df.values[idx]))


meal_db.commit()
meal_db.close()

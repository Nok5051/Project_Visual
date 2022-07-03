# https://yurimkoo.github.io/python/2019/09/14/connect-db-with-python.html

#pip install PyMySQL

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

cursor = meal_db.cursor(pymysql.cursors.DictCursor)


sql = "select * from Map_store;"

cursor.execute(sql)
result = cursor.fetchall()
print(result)





import pymysql
import pandas as pd
import csv


meal_db = pymysql.connect(
    user='mealproject',
    passwd='meal1234',
    host='localhost',
    db='meal',
    charset='utf8'
)

curs = meal_db.cursor()

sql = "insert into mealproject_recipetable (RECIPE_NM, QNT, RECIPE) values (%s, %s, %s);"

f = open('data/df_rc.csv', 'r', encoding='utf-8')
rd = csv.reader(f)

print(rd)

for line in rd:
    print(line)
    curs.execute(sql, (line[1], line[2], line[3]))


meal_db.commit()
meal_db.close()
f.close()
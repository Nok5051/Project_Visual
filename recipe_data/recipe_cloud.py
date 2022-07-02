import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


df = pd.read_csv('./recipe_data/standard_price.csv')
# print(df.head(10))

ingre = df['name']
ingre_list = ingre.values.tolist()

count_list = []

for a in ingre_list :
    target_url = f'https://www.10000recipe.com/recipe/list.html?q={a}'
    resp = requests.get(target_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    recipe = soup.find('div', {'class' : 'm_list_tit'})
    count = recipe.find('b').text
    count_list.append(int(count.replace(',','')))

# print(count_list)

recipe_dic = dict(zip(ingre_list,count_list))
print(recipe_dic)

cloud = WordCloud(background_color='white', max_words=30, width=400, height=300, font_path='./recipe_data/Goyang.ttf').fit_words(recipe_dic)

'''
visual = cloud.fit_words(recipe_dic)
visual.to_image()
visual.to_file('recipe.png')
'''

plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
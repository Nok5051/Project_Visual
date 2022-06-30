import pandas as pd
import numpy as np

df = pd.read_csv('ingredient_price_2.csv')

df = df.drop(['메이커', '스펙'], axis=1)
df = df.drop_duplicates(['품목'])

df.loc[df['품목'] == '밀가루', '단위'] = '1kg'
df.loc[df['품목'] == '옛날국수(소면)', '단위'] = '900g'
df.loc[df['품목'] == '둥근햇반실속', '단위'] = '8개입'

# 레시피_재료명을 포함하는 칼럼이 있는지 찾고,
# 있으면 단위와 가격을 붙인다.
# 여러개 있으면 작은 가격을 붙인다.

df2 = pd.read_csv('recipe_ingredient.csv')
item_list = df2['재료명'].values.tolist()
quantity_list = []
price_list = []

for item in item_list:
    temp_df = df[df['품목'].str.contains(item)]
    #print(temp_df)
    if(len(temp_df) == 0):
        quantity_list.append('no data')
        price_list.append('no data')
    elif(len(temp_df) == 1):
        quantity_list.append(temp_df.iloc[0,1])
        price_list.append(temp_df.iloc[0,2])
    else:
        temp_df = temp_df.sort_values(by=['가격'])
        quantity_list.append(temp_df.iloc[0, 1])
        price_list.append(temp_df.iloc[0, 2])

dict = {'재료명':item_list,
        '단위':quantity_list,
        '가격':price_list}
df_recipe_ingredient = pd.DataFrame.from_dict(dict)
mask = df_recipe_ingredient['단위'].isin(['no data'])
df_has_value = df_recipe_ingredient[~mask]
# print(df_has_value)


df_has_value.to_csv('price_2.csv', index=False, encoding='utf-8-sig')

import pandas as pd

def load_columns():
    df = pd.read_csv("data/retaurant.csv", encoding='utf-8', index_col=0)
    df.drop(['index'], axis=1, inplace=True)

    return df
    #print(df)

def del_columns(df):





if __name__ == '__main__':
    load_columns()

    del_columns(df)
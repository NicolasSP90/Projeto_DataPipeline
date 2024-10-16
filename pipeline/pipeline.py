import pandas as pd
import numpy as np
import os


def data_df(data):
    df = pd.DataFrame(data)
    return df


def save_data(df, nome):
    file = f"../data/{nome}.parquet"
    if file in os.listdir(os.path.join(os.path.curdir, "..", "data")):
        pass
    else:
        df.to_parquet(f"../data/{nome}.parquet")


def get_date_shape(df):
    df = pd.read_parquet("../data/data_raw.parquet")





def extract_font(df):
    def nome_fonte(fonte):
        return fonte.get('name')
    
    df['source'] = df['source'].apply(nome_fonte)

    return df
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

def verificar_e_excluir_duplicadas(df):
    duplicados = df[df.duplicated(keep=False)]
    
    num_duplicados = df.duplicated().sum()
    
    if num_duplicados > 0:
        print(f"Total de linhas duplicadas: {num_duplicados}")
        print(duplicados)
        
        df = df.drop_duplicates()
        print("Linhas duplicadas removidas com sucesso.")
    else:
        print("Não foram encontradas linhas duplicadas no DataFrame.")
    
    return df

def valores_nulos(df):
    nulos = df.isnull().sum()
    print (nulos)


def remover_coluna(df):
    return df.drop(columns=['urlToImage'])

def alterar_nome_colunas(df):
    renomear_colunas = {
        'author': 'Autor',
        'title': 'Título',
        'description': 'Descrição',
        'url' : 'URL',
        'publishedAt': 'Data Publicação',
        'content': 'Conteúdo',
        'source': 'Fonte'
}
    df = df.rename(columns=renomear_colunas)
    return df
    
def organizar_colunas(df):
    ordenamento_colunas = ['Data Publicação', 'Título', 'Autor', 'Descrição', 'URL', 'Fonte', 'Conteúdo']

    df = df[ordenamento_colunas]
    return df

def data (df):
    df['Data Publicação'] = pd.to_datetime(df['Data Publicação'], format='ISO8601')
    df['Data Publicação'] = df['Data Publicação'].dt.strftime('%Y/%m/%d')
    
    return df

def ordenar_data(df):
    df = df.sort_values('Data Publicação').reset_index().drop(columns=['index'])
    return df


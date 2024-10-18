import pandas as pd
import numpy as np
import datetime
import os

class Data_Pipeline_API:
    def __init__(self) -> None:
        self.__df = None
        self.__df_parquet = None

    
    def load_api(self, data) -> None:
        # Funçao para corrigir a coluna source de dicionario para apenas o valor da chave "name"
        def extract_font(df):
            def nome_fonte(fonte):
                return fonte.get('name')
            df['source'] = df['source'].apply(nome_fonte)
            return df
        self.__df = extract_font(pd.DataFrame(data))


    # Transformar os dados .parquet em DataFrame
    def load_parquet(self, name) -> None:
        file = f"{name}.parquet"
        data_folder = os.path.join(os.path.curdir, "..", "data")
        self.__df_parquet = pd.read_parquet(os.path.join(data_folder, file))


    # Concatenando o DataFrame com o arquivo parquet
    # Mantém apenas colunas únicas
    def save_data(self, name) -> None:
        file = f"{name}.parquet"
        data_folder = os.path.join(os.path.curdir, "..", "data")
        if file in os.listdir(data_folder):
            self.load_parquet(name)
            self.__df = pd.concat([self.__df_parquet, self.__df]).drop_duplicates().reset_index().drop(columns=["index"])
        self.__df.to_parquet(os.path.join(data_folder, file))


    def data_cleaning(self):
        # Remove coluna de url de imagem de capa
        self.__df_parquet = self.__df_parquet.drop(columns=['urlToImage'])

        #Alterar o nome das colunas
        self.__df_parquet = self.__df_parquet.rename(columns={'author': 'Autor',
                                              'title': 'Título',
                                              'description': 'Descrição',
                                              'url' : 'URL',
                                              'publishedAt': 'Data Publicação',
                                              'content': 'Conteúdo',
                                              'source': 'Fonte'})

        # Organizar colunas
        df_order = ['Data Publicação', 'Título', 'Autor', 'Descrição', 'URL', 'Fonte', 'Conteúdo']
        self.__df_parquet = self.__df_parquet[df_order]

        # Ajuste do dia de publicação
        self.__df_parquet['Data Publicação'] = pd.to_datetime(self.__df_parquet['Data Publicação'], format='ISO8601')
        self.__df_parquet['Data Publicação'] = self.__df_parquet['Data Publicação'].dt.strftime('%Y/%m/%d')

        # Ordenar Datas
        self.__df_parquet = self.__df_parquet.sort_values('Data Publicação').reset_index().drop(columns=['index'])
    

    @property
    def df(self):
        return self.__df


    @property
    def df_parquet(self):
        return self.__df_parquet
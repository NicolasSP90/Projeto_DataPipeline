# Bibliotecas
import datetime


# Variáveis
from env.env_variables import apikey


# Funções
from api import api
from pipeline import pipeline

# Instanciando API
client = api.api_client(apikey)

# Adquirindo Artigos
articles = api.get_articles(client)

# Iniciando a Pipeline
df = pipeline.data_df(articles)

# Extraindo dados brutos
pipeline.save_data(df, "raw_data")

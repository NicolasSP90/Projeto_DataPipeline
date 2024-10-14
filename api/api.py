# Bibliotecas
from newsapi import NewsApiClient

def funcao_api(apikey):
    # Inicializando News API
    newsapi = NewsApiClient(api_key=apikey)
    
    return newsapi

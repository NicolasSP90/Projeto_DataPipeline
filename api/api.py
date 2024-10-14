# Bibliotecas
from newsapi import NewsApiClient
import json

def api_client(key):
    # Inicializando News API
    newsapi = NewsApiClient(api_key=key)
    return newsapi

def total_results(client):
    # TODO
    # Função para percorrer todas as páginas
    # E depois chamar a função para extrair os artigos
    pass


def get_articles(client):
    #TODO
    # Alterar para ser apenas a extração dos artigos
    all_articles = client.get_everything(q="genomics")
    if all_articles["status"] == "ok":
        return all_articles["articles"]
    else:
        raise ValueError("Status não Encontrado")
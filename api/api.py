# Bibliotecas
from newsapi import NewsApiClient
import json


def api_client(key):
    # Inicializando News API
    newsapi = NewsApiClient(api_key=key)
    return newsapi


def search(client, page = 1):
    try: 
        all_data = client.get_everything(q="genomics", page = page)
        return all_data
    except:
        return {"status": "end"}


def get_articles(client):
    all_data = search(client)
    page = 1
    all_articles = []
    while all_data["status"] == "ok":
        all_articles += all_data["articles"]
        page += 1
        all_data = search(client, page)
    return all_articles
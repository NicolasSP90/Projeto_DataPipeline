# Bibliotecas
from newsapi import NewsApiClient
import os
import datetime

class APIClient:
    def __init__(self, key, query) -> None:
        self.__client = NewsApiClient(api_key=key)
        self.__query = query
        self.__all_data = None
        self.__articles = []

    def search(self, page):
        try:
            self.__all_data = self.__client.get_everything(q=self.__query, page = page)
        except:
            self.__all_data = {"status": "end"}


    def get_articles(self):
        page = 1
        self.search(page=page)
        while self.__all_data["status"] == "ok":
            self.__articles += self.__all_data["articles"]
            page += 1
            self.search(page=page)

    @property
    def articles(self):
        return self.__articles
    
    @property
    def all_data(self):
        return self.__all_data
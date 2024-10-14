# Bibliotecas


# Variáveis
from env.env_variables import apikey

# Funções
from api.api import api_client, get_articles

client = api_client(apikey)



articles = get_articles(client)
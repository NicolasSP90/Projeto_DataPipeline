# Bibliotecas
import datetime
import time

# Variáveis
from env.env_variables import apikey

# Funções
from api.api import APIClient
from env.criteria import Search_Criteria
from pipeline.pipeline import Data_Pipeline_API

# Instanciando pesquisa e palavras chave
criteria = Search_Criteria("genomics", ["DNA", "genetic", "treatment"])

# Instanciando API
client = APIClient(apikey, criteria.subject)

# Defina os minutos específicos em que a ação deve ocorrer
specific_time = [0, 15, 30, 45]

print("Script Iniciado")

while True:
    now = datetime.datetime.now()
    current_minute = now.minute  # Obtém o minuto atual
    
    if current_minute in specific_time:
        # Adquirindo todos os artigos
        client.get_articles()

        # Instanciando Pipeline
        pipeline_data = Data_Pipeline_API()

        if len(client.articles) != 0:
            # Carregando dados da API
            pipeline_data.load_api(client.articles)

            # Salvando em Parquet - Dados brutos
            pipeline_data.save_data("raw_data")
            print(f"raw_data atualizado em {now.strftime('%Y-%m-%d %H:%M:%S')}")

        if current_minute == 0:
            # Importando DataFrame
            pipeline_data.load_parquet("raw_data")

            # Limpeza de dados
            pipeline_data.data_cleaning()

            # Salvando Parquet
            pipeline_data.save_data("cleaned_data")
            print(f"cleaned_data atualizado em {now.strftime('%Y-%m-%d %H:%M:%S')}")
        
            # Pausa de 12 minutos segundos para evitar múltiplas execuções no mesmo minuto
            time.sleep(720)
        
        else:
            # Verifica a cada 30 segundos
            time.sleep(30)


# Bibliotecas
from datetime import datetime
import time
import schedule

# Variáveis
from env.env_variables import apikey

# Funções
from api.api import APIClient
from env.criteria import Search_Criteria
from pipeline.pipeline import Data_Pipeline_API

# Funçoes de rotina
def update_raw():
    now = datetime.now()

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
    
    else:
        print(f"Sem atualizações em {now.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(30)


def update_cleaned():
    update_raw()
    now = datetime.now()

    # Instanciando Pipeline
    pipeline_data = Data_Pipeline_API()
    
    # Importando DataFrame
    pipeline_data.load_parquet("raw_data")

    # Limpeza de dados
    pipeline_data.data_cleaning()

    # Salvando Parquet
    pipeline_data.save_data("cleaned_data")
    print(f"cleaned_data atualizado em {now.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(780)


# Instanciando pesquisa e palavras chave
criteria = Search_Criteria("genomics", ["DNA", "genetic", "treatment"])

# Instanciando API
client = APIClient(apikey, criteria.subject)

print("Script Iniciado")

schedule.every().hour.at(":00").do(update_cleaned)
schedule.every().hour.at(":15").do(update_raw)
schedule.every().hour.at(":30").do(update_raw)
schedule.every().hour.at(":45").do(update_raw)

while True:
    schedule.run_pending()
    time.sleep(20) 
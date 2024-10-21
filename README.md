![pyenv](https://img.shields.io/badge/pyenv-white?style=for-the-badge)
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)
![ipykernel](https://img.shields.io/badge/ipykernel-3670A0?style=for-the-badge)
![newsapi](https://img.shields.io/badge/newsapi-1a73e8?style=for-the-badge)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![pyarrow](https://img.shields.io/badge/pyarrow-222832?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![poo](https://img.shields.io/badge/poo-black?style=for-the-badge)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=flat-square&logo=apachespark&logoColor=black)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Databricks](https://img.shields.io/badge/databricks-222832?style=for-the-badge&logo=databricks)


# Contexto do Projeto

O grupo trabalha no time de engenharia de dados na HealthGen, uma empresa especializada em genômica e pesquisa de medicina personalizada. A genômica é o estudo do conjunto completo de genes de um organismo, desempenha um papel fundamental na medicina personalizada e na pesquisa biomédica. Permite a análise do DNA para identificar variantes genéticas e mutações associadas a doenças e facilita a personalização de tratamentos com base nas características genéticas individuais dos pacientes.

A empresa precisa se manter atualizada sobre os avanços mais recentes na genômica, identificar oportunidades para pesquisa e desenvolvimento de tratamentos personalizados e acompanhar as tendências em genômica que podem influenciar estratégias de pesquisa e desenvolvimento. Pensando nisso, o time de dados apresentou uma proposta de desenvolvimento de um sistema que coleta, analisa e apresenta as últimas notícias relacionadas à genômica e à medicina personalizada, e também estuda o avanço do campo nos últimos anos. 

O time de engenharia de dados tem como objetivo desenvolver e garantir um pipeline de dados confiável e estável. As principais atividades são:

## 1. Consumo de dados com a News API: 
Implementar um mecanismo para consumir dados de notícias de fontes confiáveis e especializadas em genômica e medicina personalizada, a partir da News API: 
https://newsapi.org/

## 2. Definir Critérios de Relevância:
* Desenvolver critérios precisos de relevância para filtrar as notícias. Por exemplo, o time pode se concentrar em notícias que mencionem avanços em sequenciamento de DNA, terapias genéticas personalizadas ou descobertas relacionadas a doenças genéticas específicas.

## 3. Cargas em Batches:
* Armazenar as notícias relevantes em um formato estruturado e facilmente acessível para consultas e análises posteriores. Essa carga deve acontecer 1 vez por hora. Se as notícias extraídas já tiverem sidos armazenadas na carga anterior, o processo deve ignorar e não armazenar as notícias novamente, os dados carregados não podem ficar duplicados.

## 4. Dados transformados para consulta do público final
* Quantidade de notícias por ano, mês e dia de publicação;
* Quantidade de notícias por fonte e autor;
* Quantidade de aparições de 3 palavras chaves por ano, mês e dia de publicação

# Particularidades do Projeto

## Variáveis de Ambiente
Na raíz do projeto existe deve ser criado na pasta *env* um arquivo chamado *env_variables.py*. Neste arquivo devem ser adicionadas as variáveis e valores a seguir:

* *apikey*: Chave deve ser criada no portal [News API](https://newsapi.org)

## Ambiente de Desenvolvimento
O projeto em si é modularizado e cada módulo armazena as funções específicas daquela aplicação. Para testes específicos de funções, é utilizado o notebook do diretório *tests*.

Além disso, o *.gitignore* ignora os seguintes diretórios:
* env/env_variables.py - Arquivo das variáveis e chaves necessárias.
* __ pycache __ - diretório de arquivos cache. Podem existir dentro dos diretórios dos módulos e serve para o ambiente de testes apenas.

## API - News API
A API em si possui uma biblioteca para facilitar os requests e pode ser instalada com _pip install newsapi-python_.

A API em si possui algumas limitações (Ambiente Gratuito):
* A busca por artigos é limitada aos últimos 30 dias;
* 50 requests a cada 12 horas;
* Métodos para solicitar todos os artigos é limitado a 100 artigos por página
* A última página, ao solicitar todos os artigos, possui mais de 100 artigos. Para adquirir podem ser utilizados requests personalizados. Nesse caso foi decidido não fazer uma estratégia de aquisição por dois motivos: Podem ultrapassar os requests necessários; Não garante que todos os artigos serão adquiridos, sendo necessário o comando de aquisição de todos de uma forma ou de outra.

O foco do projeto não é necessariamente a API, sendo assim as limitações delas serão relevadas.





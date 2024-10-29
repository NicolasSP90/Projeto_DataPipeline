![pyenv](https://img.shields.io/badge/pyenv-white?style=for-the-badge)
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)
![ipykernel](https://img.shields.io/badge/ipykernel-3670A0?style=for-the-badge)
![newsapi](https://img.shields.io/badge/newsapi-1a73e8?style=for-the-badge)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![pyarrow](https://img.shields.io/badge/pyarrow-222832?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![poo](https://img.shields.io/badge/poo-black?style=for-the-badge)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=for-the-badge&logo=apachespark&logoColor=black)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-white?style=for-the-badge&logo=jupyter&logoColor=orange)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Databricks](https://img.shields.io/badge/databricks-222832?style=for-the-badge&logo=databricks)


# Enunciado Projeto Proposto

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

# Projeto

O projeto tem como objetivo ser utilizado no Databricks. Dessa forma os notebooks são efetivamente o projeto e aplicação. As demais pastas foram feitas para desenvolvimento local de objetos e códigos para serem importados para os notebooks do Databricks e/ou testados. Algumas considerações:

* A estrutura de diretórios do Databricks não é exatamente a mesmas para importação de pacotes e objetos. Dessa forma foi optado pelos códigos de objetos serem adicionados em um notebook que é inicializado dentro de cada outro notebook em que os objetos serão utilizados.

* A idéia central é que seja realizada a menor quantidade de interações fora dos notebooks de modo que cada notebook apenas seja executado (Run All) ao ser aberto. Para isso são necessárias instalar as bibliotecas informadas diretamente no  terminal.

* Os objetos são virtualmente os mesmos. A diferença está nos objetos de pipeline que, ao serem importados para o databricks foram remodelados para utilizarem pyspark, além de salvarem os dados em delta e utilizarem o *Database Tables* para armazenar as últimas tabelas.

De maneira geral o Scheduler define os momemntos em que a aquisição de dados da API deve ser realizada. Nesses momentos, os objetos de critérios de busca (Search_Criteria) e o cliente da API (API_Client) são instanciados e de acordo com o processo em questão (Update ou Transform), os dados são adquiridos da API e encaminhados para seu mensageiro (Kafka_Producer).

![Fluxo_Scheduler](assets/01.Scheduler_Update_Transform.png)

Caso o processo seja de Update, as informações serão coletadas e os dados brutos serão armazenados.

![Fluxo_Raw](assets/02.Update.png)

Caso o processo seja de Transform, inicialmente as informações serão coletadas e os dados brutos serão armazenados. Após isso é realizada a limpeza e armazenamento dos dados limpos/transformados. Finalmente, são geradas tabelas para serem respondidas as questões de negócio.

![Fluxo_Transform](assets/03.Transform.png)

# Estrutura Local

## Ambiente de Desenvolvimento
O projeto é modularizado, com cada módulo armazenando as funções específicas da aplicação. Para testes individuais de funções, utilizamos notebook localizado no diretório *tests*.

## Variáveis de Ambiente
Na pasta chamada env, deve ser criado um arquivo *env_variables.py*. Neste arquivo, será configurada a seguinte variável de ambiente:

*apikey*: Chave deve ser criada no portal [News API](https://newsapi.org).

Chave de acesso à API, que deve ser gerada individualmente no portal News API. Cada desenvolvedor precisa criar sua própria chave de acesso no portal e inseri-la nesta variável para utilizar os serviços da API.

## Arquivos Ignorados

O arquivo .gitignore está configurado para ignorar os seguintes diretórios e arquivos:

* env/env_variables.py: Arquivo contendo as variáveis de ambiente e chaves de acesso.
* pycache: Diretórios de cache gerados automaticamente, geralmente criados dentro dos módulos, e utilizados apenas no ambiente de testes.

## Integração com a API - News API
Utilizamos a biblioteca oficial da News API para facilitar as requisições, a qual pode ser instalada com o seguinte comando:

pip install newsapi-python

Limitações da API (Plano Gratuito):
* A busca por artigos está restrita aos últimos 30 dias.
* Limite de 50 requisições a cada 12 horas.
* O retorno da API é limitado a 100 artigos por página.
* A última página pode conter mais de 100 artigos, mas não foi implementada uma estratégia para adquirir todos os artigos adicionais, devido à limitação de requisições e à falta de garantia de que todos os artigos seriam obtidos.

Essas limitações foram consideradas no desenvolvimento do projeto, e como o foco principal não é a aquisição de todos os artigos possíveis, essas restrições não comprometem o objetivo final.

# Databricks
 Abaixo estão os detalhes de cada notebook que deve ser importado ao Databricks. OBS: para simplificar execução dos notebooks no databricks, os objetos (cliente api, pipeline, etc) se encontram em código dentro das células dos notebooks.

### 01.setup_kafka_zookeeper.ipynb

Neste arquivo, o Apache Kafka é baixado, descompactado e instalado no cluster do Databricks. Além disso, o funcionamento do Zookeeper, que é responsável pela coordenação dos serviços distribuídos, é iniciado.

### 02.setup_kafka_server.ipynb

Este arquivo contém o comando necessário para iniciar o servidor Kafka, permitindo a comunicação entre o cluster e os consumidores/produtores de mensagens.

### 03.setup_kafka_topics.ipynb

Aqui, os tópicos Kafka utilizados no projeto são criados, onde as mensagens da API serão publicadas e consumidas.

### 04.objects.ipynb

Nesse notebook estão os objetos necessários para as aplicações. Seu função é ser importada pelos demais notebooks para que os objetos sejam utilizados.

### 05.consumer_gather_data.ipynb e 06.consumer_clean_data.ipynb

Ambos arquivos possuem o objeto da pipeline, para consumo e processamento de dados. A separação em dois arquivos se dá por conta dos consumers serem diferentes para aquisição e salvamento de dados brutos e para limpeza e salvamento de dados tratados. 

Para garantir o funcionamento correto, é necessário instalar quatro bibliotecas no ambiente Databricks, através do terminal:
* pip install --upgrade pip
* pip install kafka-python
* pip install newsapi-python
* pip install schedule

A pipeline converte os dados da API em arquivo parquet de dados brutos (*Extract*), limpa dados para realizar o salvamento em arquivo parquet, tabela delta e disponibiliza no *Database Tables* (*Transform*) e finalmente filtra e cria as tabelas no *Database Tables* para responder as perguntas de negócio (*Load*)

### 07.insertion.ipynb

Neste arquivo, são definidos os critérios de busca de artigos na API NewsAPI, o produtor de mensagens Kafka (producer), e a rotina de carga de dados brutos e de limpeza e tratamento dos dados.

### 08.visualization.ipynb

Aqui são visualizados as tableas salvas, como a visualização das publicações de artigos, autores e palavras-chave.

# Conclusão
Este projeto foi desenvolvido com o objetivo de integrar a News API ao Kafka e permitir o processamento de dados dentro de um ambiente distribuído como o Databricks. Seguindo as instruções fornecidas ao longo deste documento, é possível configurar o ambiente corretamente e garantir o funcionamento eficiente da pipeline de dados.

Apesar das limitações da API no plano gratuito, o projeto foi planejado para ser escalável e modular, facilitando a manutenção e a adição de novas funcionalidades no futuro. O uso de tecnologias como Kafka e Databricks permite um processamento em tempo real e em lote, tornando o projeto uma base sólida para quem deseja explorar a integração de APIs e processamento de dados em larga escala.

Agradecemos o interesse no projeto e ficamos à disposição para sugestões ou melhorias. Sinta-se à vontade para contribuir, testar e personalizar conforme suas necessidades.






# Projeto de Integração de Dados: MongoDB e MySQL

## Descrição

Este projeto tem como objetivo realizar a extração de dados de uma API, transformá-los e carregá-los em um banco de dados MySQL, utilizando um fluxo ETL (Extract, Transform, Load). Os dados são inicialmente obtidos de um serviço JSON fornecido por uma API pública e, em seguida, inseridos em uma coleção do MongoDB. Posteriormente, os dados são transformados e salvos em um arquivo CSV, que é então carregado em uma tabela no MySQL.

## Tecnologias Utilizadas

- Python
- MongoDB
- MySQL
- Pandas
- Requests
- Pymongo
- mysql-connector-python

## Estrutura do Projeto

├── data
│ └── produto_preço.csv # Arquivo CSV gerado com os dados transformados
├── notebooks
│ ├── 01_extração.ipynb # Notebook para extração de dados e análise preliminar
│ ├── 02_transformação.ipynb # Notebook para transformação de dados
│ └── 03_carregamento.ipynb # Notebook para carregamento de dados no MySQL
├── src
│ ├── extract_and_save.py # Script para extrair dados da API e salvar no MongoDB
│ ├── transform_data.py # Script para transformar os dados do MongoDB e salvar em CSV
│ └── save_data_mysql.py # Script para carregar os dados do CSV para o MySQL
└── README.md




## Instalação

### Pré-requisitos

- Python 3.12
- MongoDB Atlas ou instalação local do MongoDB
- MySQL Server

### Dependências

Instale as dependências necessárias com o seguinte comando:


pip install pymongo mysql-connector-python pandas requests
## Uso

Para realizar as operações de ETL, siga os passos abaixo:

### 1. Extrair e Salvar Dados no MongoDB
Execute o script `extract_and_save.py` para extrair dados da API e salvá-los no banco de dados MongoDB.


python extract_and_save.py


### 2. Transformar os Dados e Salvar em CSV

Execute o script transform_data.py para transformar os dados do MongoDB e salvá-los em um arquivo CSV.

python transform_data.py


### 3. Salvar os Dados no MySQL

Execute o script save_data_mysql.py para carregar os dados do arquivo CSV para o banco de dados MySQL.

python save_data_mysql.py




### Observações:
- **Estrutura do projeto**: A estrutura de pastas e arquivos é mostrada para facilitar a navegação pelo repositório.
- **Instruções de uso**: Cada script possui uma breve descrição e instruções de como executá-los.



### Contato:

Para mais informações, entre em contato:

Nome: Gustavo Pasciano
Email: gustavohqpasciano@gmail.com
linkedin: https://www.linkedin.com/in/gustavo-henrique-pasciano-463b31193/


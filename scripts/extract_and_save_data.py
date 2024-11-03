
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

def connect_mongo(uri):
    """
    Conecta ao MongoDB e verifica a conexão com um comando ping.
    """
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Conexão bem-sucedida com o MongoDB!")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        client = None
    return client

def create_connect_db(client, db_name):
    """
    Retorna uma referência para o banco de dados especificado.
    """
    return client[db_name]

def create_connect_collection(db, col_name):
    """
    Retorna uma referência para a coleção especificada.
    """
    return db[col_name]

def extract_api_data(url):
    """
    Faz uma requisição à API e retorna os dados em JSON.
    """
    response = requests.get(url)
    return response.json()

def insert_data(col, data):
    """
    Insere dados na coleção especificada e retorna o número de documentos inseridos.
    """
    result = col.insert_many(data)
    n_docs_inseridos = len(result.inserted_ids)
    return n_docs_inseridos

def main():
    # Configurações
    uri = "caminho do mongo compass"
    db_name = "db_produtos"
    col_name = "produtos"
    api_url = 'https://dummyjson.com/products?limit=10&skip=10&select=title,price'

    # Conexão com o MongoDB
    client = connect_mongo(uri)
    if client is None:
        print("Falha ao conectar ao MongoDB.")
        return

    # Conecta ao banco de dados e à coleção
    db = create_connect_db(client, db_name)
    collection = create_connect_collection(db, col_name)

    # Extrai dados da API
    dados_totais = extract_api_data(api_url)
    produtos = dados_totais.get("products", [])

    # Insere dados na coleção e exibe resultados
    if produtos:
        n_inseridos = insert_data(collection, produtos)
        print(f"Número de documentos inseridos: {n_inseridos}")
    else:
        print("Nenhum dado encontrado para inserir.")

    # Fecha a conexão com o MongoDB
    client.close()

# Executa a função principal
if __name__ == "__main__":
    main()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

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

def fetch_data(collection):
    """
    Extrai os dados da coleção MongoDB e os transforma para o formato necessário.
    """
    data = [{"id": doc["id"], "title": doc["title"], "price": doc["price"]} for doc in collection.find()]
    return data

def save_to_csv(data, filepath):
    """
    Salva os dados transformados em um arquivo CSV.
    """
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"Dados salvos em {filepath}")

def main():
    # Configurações
    uri = "mongodb+srv://gustavohqpasciano:P50Po7A9rGTPaQOq@cluster-produtos.hyph6.mongodb.net/?retryWrites=true&w=majority&appName=cluster-produtos"
    db_name = "db_produtos"
    col_name = "produtos"
    output_path = "../data/produto_preço.csv"

    # Conexão com o MongoDB
    client = connect_mongo(uri)
    if client is None:
        print("Falha ao conectar ao MongoDB.")
        return

    # Conecta ao banco de dados e à coleção
    db = create_connect_db(client, db_name)
    collection = create_connect_collection(db, col_name)

    # Extração e transformação dos dados
    dados_para_csv = fetch_data(collection)

    # Salva os dados no CSV
    save_to_csv(dados_para_csv, output_path)

    # Fecha a conexão com o MongoDB
    client.close()

# Executa a função principal
if __name__ == "__main__":
    main()

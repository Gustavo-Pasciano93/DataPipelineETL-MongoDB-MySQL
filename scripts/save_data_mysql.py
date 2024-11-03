import mysql.connector
import pandas as pd

def connect_mysql(host, user, password, database):
    """
    Estabelece conexão com o banco de dados MySQL.
    """
    try:
        conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Conexão estabelecida com o MySQL.")
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None

def create_table(cursor):
    """
    Cria a tabela no banco de dados MySQL se ela ainda não existir.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabela_mongo (
            id VARCHAR(100) PRIMARY KEY,
            title VARCHAR(100),
            price FLOAT(10,2)
        )
    """)
    print("Tabela criada/verificada com sucesso.")

def load_csv(filepath):
    """
    Carrega os dados do arquivo CSV em um DataFrame.
    """
    df = pd.read_csv(filepath)
    print(f"Dados carregados do arquivo {filepath}.")
    return df

def prepare_data_for_insertion(df):
    """
    Prepara os dados do DataFrame para inserção no MySQL,
    convertendo cada linha em uma tupla.
    """
    lista_dados = [tuple(row) for _, row in df.iterrows()]
    print("Dados preparados para inserção no MySQL.")
    return lista_dados

def insert_data(cursor, lista_dados):
    """
    Insere os dados no banco de dados MySQL.
    """
    sql = "INSERT INTO tabela_mongo (id, title, price) VALUES (%s, %s, %s)"
    cursor.executemany(sql, lista_dados)
    print(f"{cursor.rowcount} registros inseridos.")

def main():
    # Configurações
    host = "localhost"
    user = "xxxxx"
    password = "xxxxxx"
    database = "xxxxxxxx"
    csv_filepath = "../data/produto_preço.csv"

    # Conexão com o MySQL
    conexao = connect_mysql(host, user, password, database)
    if conexao is None:
        print("Falha ao conectar ao MySQL.")
        return

    cursor = conexao.cursor()

    # Cria a tabela se não existir
    create_table(cursor)

    # Carrega os dados do CSV
    df_produto = load_csv(csv_filepath)

    # Prepara os dados para inserção
    lista_dados = [tuple(row) for _, row in df_produto.iterrows()]

    # Insere os dados na tabela
    insert_data(cursor, lista_dados)

    # Confirma as transações e fecha a conexão
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Conexão fechada e dados salvos com sucesso.")

# Executa a função principal
if __name__ == "__main__":
    main()

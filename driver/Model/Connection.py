from psycopg import connect, OperationalError
from dotenv import load_dotenv
import os

class Connection:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DB_HOST")
        self.dbname = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.port = int(os.getenv("DB_PORT")) 
        self.conn = None

    def connect(self):
        try:
            self.conn = connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )
            print("✅ Conexão com o banco de dados estabelecida com sucesso!")
            return self.conn
        except OperationalError as e:
            print("ERRO 500 - Falha na conexão com o banco de dados")
            print(f"Detalhes técnicos: {e}")
            input("Pressione ENTER para continuar.")
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("🔌 Conexão encerrada.")

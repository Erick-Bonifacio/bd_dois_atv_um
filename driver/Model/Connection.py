import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError

class Connection:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DB_HOST")
        self.dbname = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.port = os.getenv("DB_PORT") or "5432"
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password='root'
            )
            print("Conexão estabelecida com sucesso.")
            return self.conn
        except OperationalError as e:
            print(e)
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexão encerrada.")

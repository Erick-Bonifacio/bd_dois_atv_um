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
        self.conn = None

    def connect(self):
        try:
            self.conn = connect(
                host=self.host,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            return self.conn
        except OperationalError:
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("🔌 Conexão encerrada.")

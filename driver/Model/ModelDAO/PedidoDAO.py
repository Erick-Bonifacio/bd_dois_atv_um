from driver.Model.Connection import Connection
from psycopg.errors import Error
from datetime import datetime

class PedidoDAO:
    def __init__(self):
        self.db = Connection()

    def testar_conexao(self):
        try:
            conn = self.db.connect()
            if conn:
                conn.close()
                return True
            return False
        except Exception:
            return False

    def buscar_pedido_completo(self, codigo_pedido):
        consulta = """
            SELECT 
                p.orderid, 
                p.orderdate, 
                cli.contactname AS nome_cliente, 
                emp.firstname AS nome_funcionario,
                det.productid, 
                det.unitprice, 
                det.quantity
            FROM orders p
            JOIN customers cli ON p.customerid = cli.customerid
            JOIN employees emp ON p.employeeid = emp.employeeid
            LEFT JOIN order_details det ON p.orderid = det.orderid
            WHERE p.orderid = """ + str(codigo_pedido) + ";"
        return self.__executar_sql(consulta, fetch=True)


    def inserir_pedido(self, dados):
        conn = self.db.connect()
        if not conn:
            raise Exception("❌ Falha na conexão com o banco de dados")

        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("SET search_path TO northwind;")

                    comando_pedido = """
                        INSERT INTO orders 
                        (orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, 
                        shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """
                    cur.execute(comando_pedido, dados['order'])

                    comando_itens = """
                        INSERT INTO order_details (orderid, productid, unitprice, quantity, discount)
                        VALUES (%s, %s, %s, %s, %s);
                    """
                    for item in dados['order_details']:
                        cur.execute(comando_itens, item)

        except Exception as erro:
            if conn:  # garante que só tenta rollback se a conexão existir
                try:
                    conn.rollback()
                except:
                    pass
            raise Exception(f"❌ Erro ao inserir pedido. Detalhes: {erro}")

        finally:
            if conn:
                try:
                    conn.close()
                except:
                    pass


    def ranking_funcionarios(self, data_inicio, data_fim):
        consulta = """
            SELECT 
                emp.firstname || ' ' || emp.lastname AS nome_funcionario,
                emp.hiredate,
                COUNT(DISTINCT ped.orderid) AS total_pedidos,
                SUM(det.unitprice * det.quantity * (1 - det.discount)) AS total_vendido
            FROM employees emp
            JOIN orders ped ON emp.employeeid = ped.employeeid
            JOIN order_details det ON ped.orderid = det.orderid
            WHERE emp.hiredate BETWEEN %s AND %s
            GROUP BY emp.firstname, emp.lastname, emp.hiredate
            ORDER BY total_vendido DESC;
        """
        return self.__executar_sql(consulta, valores=(data_inicio, data_fim), fetch=True)




    from psycopg.errors import Error 

    def __executar_sql(self, comando, valores=(), fetch=False):
        erro_codigo = None
        total_afetado = 0
        registros = []

        conn = self.db.connect()
        if not conn:
            return "CONN_ERR", 0, []

        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute("SET search_path TO northwind;")
                    cur.execute(comando, valores)
                    total_afetado = cur.rowcount
                    if fetch:
                        registros = cur.fetchall()
        except Error as erro:
            erro_codigo = getattr(erro, "pgcode", "UNKNOWN")
            print(f"Erro ao executar SQL: {erro_codigo} - {getattr(erro, 'pgerror', str(erro))}")
            conn.rollback()
        finally:
            conn.close()

        return erro_codigo, total_afetado, registros


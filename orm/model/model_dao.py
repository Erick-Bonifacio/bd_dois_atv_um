from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from model.models_northwind import Base, Orders, OrderDetails, Customers, Employees

class OrderDAO:
    def __init__(self):
        self.engine = create_engine('postgresql+psycopg2://postgres:ADMIN@localhost/northwind')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_order(self, order_data, order_details):
        session = self.Session()
        try:
            order = Orders(**order_data)
            session.add(order)
            session.commit()

            for detail in order_details:
                od = OrderDetails(orderid=order.orderid, **detail)
                session.add(od)
            session.commit()
        except Exception as e:
            print(f"Erro ao inserir o pedido: {e}")
            raise e
        finally:
            session.close()

    def get_order_info(self, orderid):
        session = self.Session()
        try:
            order = session.query(Orders) \
                           .join(Orders.customers) \
                           .join(Orders.employees) \
                           .join(Orders.orderDetails) \
                           .join(OrderDetails.products) \
                           .filter(Orders.orderid == orderid) \
                           .first()

            if not order:
                return None

            order_info = {
                "Número do pedido": order.orderid,
                "Data do pedido": order.orderdate.strftime("%Y-%m-%d") if order.orderdate else "N/A",
                "Nome do cliente": order.customers.companyname,
                "Nome do vendedor": f"{order.employees.firstname} {order.employees.lastname}",
                "Itens do pedido": [{"Produto": detail.products.productname, "Quantidade": detail.quantity, "Preço": float(detail.unitprice)} for detail in order.orderDetails]
            }
            return order_info
        finally:
            session.close()

    def employee_ranking(self, start_date, end_date):
        session = self.Session()
        try:
            ranking = session.query(
                Employees.firstname, Employees.lastname,
                func.count(Orders.orderid).label('total_orders'),
                func.sum(OrderDetails.unitprice * OrderDetails.quantity).label('total_sales')
            ).join(Employees.orders) \
            .join(Orders.orderDetails) \
            .filter(Orders.orderdate.between(start_date, end_date)) \
            .group_by(Employees.firstname, Employees.lastname).all()
            return ranking
        finally:
            session.close()

    def order_id_exists(self, order_id):
        session = self.Session()
        try:
            exists = session.query(Orders.orderid).filter_by(orderid=order_id).scalar() is not None
            return exists
        finally:
            session.close()
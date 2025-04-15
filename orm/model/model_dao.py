from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from orm.model.models_northwind import Base, Order, OrderDetail, Customer, Employee

class OrderDAO:
    def __init__(self):
        self.engine = create_engine('postgresql+psycopg2://postgres:ADMIN@localhost/northwind')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_order(self, order_data, order_details):
        session = self.Session()
        try:
            order = Order(**order_data)
            session.add(order)
            session.commit()

            for detail in order_details:
                od = OrderDetail(orderid=order.orderid, **detail)
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
            order = session.query(Order) \
                           .join(Order.customer) \
                           .join(Order.employee) \
                           .join(Order.details) \
                           .join(OrderDetail.product) \
                           .filter(Order.orderid == orderid) \
                           .first()

            if not order:
                return None

            order_info = {
                "Número do pedido": order.orderid,
                "Data do pedido": order.orderdate.strftime("%Y-%m-%d") if order.orderdate else "N/A",
                "Data requerida": order.requireddate.strftime("%Y-%m-%d") if order.requireddate else "N/A",
                "Data de envio": order.shippeddate.strftime("%Y-%m-%d") if order.shippeddate else "N/A",
                "Frete": float(order.freight) if order.freight else "N/A",
                "Nome do cliente": order.customer.companyname,
                "Nome do vendedor": f"{order.employee.firstname} {order.employee.lastname}",
                "Nome do destinatário": order.shipname,
                "Endereço do destinatário": order.shipaddress,
                "Cidade do destinatário": order.shipcity,
                "Região do destinatário": order.shipregion,
                "CEP do destinatário": order.shippostalcode,
                "País do destinatário": order.shipcountry,
                "ID do transportador": order.shipperid,
                "Itens do pedido": [{"Produto": detail.product.productname, "Quantidade": detail.quantity, "Preço": float(detail.unitprice)} for detail in order.details]
            }
            return order_info
        finally:
            session.close()

    def employee_ranking(self, start_date, end_date):
        session = self.Session()
        try:
            ranking = session.query(
                Employee.firstname, Employee.lastname,
                func.count(Order.orderid).label('total_orders'),
                func.sum(OrderDetail.unitprice * OrderDetail.quantity).label('total_sales')
            ).join(Employee.orders) \
            .join(Order.details) \
            .filter(Order.orderdate.between(start_date, end_date)) \
            .group_by(Employee.firstname, Employee.lastname).all()
            return ranking
        finally:
            session.close()

    def order_id_exists(self, order_id):
        session = self.Session()
        try:
            exists = session.query(Order.orderid).filter_by(orderid=order_id).scalar() is not None
            return exists
        finally:
            session.close()
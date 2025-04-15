from typing import List, Optional

from sqlalchemy import DateTime, ForeignKeyConstraint, Integer, Numeric, PrimaryKeyConstraint, SmallInteger, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal

class Base(DeclarativeBase):
    pass


class Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = (
        PrimaryKeyConstraint('categoryid', name='categories_pkey'),
        {'schema': 'northwind'}
    )

    categoryid: Mapped[int] = mapped_column(Integer, primary_key=True)
    categoryname: Mapped[Optional[str]] = mapped_column(String(50))
    description: Mapped[Optional[str]] = mapped_column(String(100))


class Customers(Base):
    __tablename__ = 'customers'
    __table_args__ = (
        PrimaryKeyConstraint('customerid', name='customers_pkey'),
        {'schema': 'northwind'}
    )

    customerid: Mapped[str] = mapped_column(String(5), primary_key=True)
    companyname: Mapped[Optional[str]] = mapped_column(String(50))
    contactname: Mapped[Optional[str]] = mapped_column(String(30))
    contacttitle: Mapped[Optional[str]] = mapped_column(String(30))
    address: Mapped[Optional[str]] = mapped_column(String(50))
    city: Mapped[Optional[str]] = mapped_column(String(20))
    region: Mapped[Optional[str]] = mapped_column(String(15))
    postalcode: Mapped[Optional[str]] = mapped_column(String(9))
    country: Mapped[Optional[str]] = mapped_column(String(15))
    phone: Mapped[Optional[str]] = mapped_column(String(17))
    fax: Mapped[Optional[str]] = mapped_column(String(17))


class Employees(Base):
    __tablename__ = 'employees'
    __table_args__ = (
        PrimaryKeyConstraint('employeeid', name='employees_pkey'),
        {'schema': 'northwind'}
    )

    employeeid: Mapped[int] = mapped_column(Integer, primary_key=True)
    lastname: Mapped[Optional[str]] = mapped_column(String(10))
    firstname: Mapped[Optional[str]] = mapped_column(String(10))
    title: Mapped[Optional[str]] = mapped_column(String(25))
    titleofcourtesy: Mapped[Optional[str]] = mapped_column(String(5))
    birthdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    hiredate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    address: Mapped[Optional[str]] = mapped_column(String(50))
    city: Mapped[Optional[str]] = mapped_column(String(20))
    region: Mapped[Optional[str]] = mapped_column(String(2))
    postalcode: Mapped[Optional[str]] = mapped_column(String(9))
    country: Mapped[Optional[str]] = mapped_column(String(15))
    homephone: Mapped[Optional[str]] = mapped_column(String(14))
    extension: Mapped[Optional[str]] = mapped_column(String(4))
    reportsto: Mapped[Optional[int]] = mapped_column(Integer)
    notes: Mapped[Optional[str]] = mapped_column(Text)

    orders = relationship('Orders', back_populates='employees')


class OrderDetails(Base):
    __tablename__ = 'order_details'
    __table_args__ = (
        ForeignKeyConstraint(['orderid'], ['northwind.orders.orderid'], name='fk_order'),
        ForeignKeyConstraint(['productid'], ['northwind.products.productid'], name='fk_product'),
        PrimaryKeyConstraint('orderid', 'productid', name='order_details_pkey'),
        {'schema': 'northwind'}
    )

    orderid: Mapped[int] = mapped_column(Integer, primary_key=True)
    productid: Mapped[int] = mapped_column(Integer, primary_key=True)
    unitprice: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(13, 4))
    quantity: Mapped[Optional[int]] = mapped_column(SmallInteger)
    discount: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(10, 4))

    orders = relationship('Orders', back_populates='orderDetails')
    products = relationship('Products')


class Shippers(Base):
    __tablename__ = 'shippers'
    __table_args__ = (
        PrimaryKeyConstraint('shipperid', name='shippers_pkey'),
        {'schema': 'northwind'}
    )

    shipperid: Mapped[int] = mapped_column(Integer, primary_key=True)
    companyname: Mapped[Optional[str]] = mapped_column(String(20))
    phone: Mapped[Optional[str]] = mapped_column(String(14))


class Suppliers(Base):
    __tablename__ = 'suppliers'
    __table_args__ = (
        PrimaryKeyConstraint('supplierid', name='supplier_pk'),
        {'schema': 'northwind'}
    )

    supplierid: Mapped[int] = mapped_column(Integer, primary_key=True)
    companyname: Mapped[Optional[str]] = mapped_column(String(50))
    contactname: Mapped[Optional[str]] = mapped_column(String(30))
    contacttitle: Mapped[Optional[str]] = mapped_column(String(30))
    address: Mapped[Optional[str]] = mapped_column(String(50))
    city: Mapped[Optional[str]] = mapped_column(String(20))
    region: Mapped[Optional[str]] = mapped_column(String(15))
    postalcode: Mapped[Optional[str]] = mapped_column(String(8))
    country: Mapped[Optional[str]] = mapped_column(String(15))
    phone: Mapped[Optional[str]] = mapped_column(String(15))
    fax: Mapped[Optional[str]] = mapped_column(String(15))
    homepage: Mapped[Optional[str]] = mapped_column(String(100))


class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = (
        ForeignKeyConstraint(['customerid'], ['northwind.customers.customerid'], name='fk_customer'),
        ForeignKeyConstraint(['employeeid'], ['northwind.employees.employeeid'], name='fk_employee'),  # Adicionada a chave estrangeira
        PrimaryKeyConstraint('orderid', name='orders_pkey'),
        {'schema': 'northwind'}
    )

    orderid: Mapped[int] = mapped_column(Integer, primary_key=True)
    customerid: Mapped[str] = mapped_column(String(5))
    employeeid: Mapped[int] = mapped_column(Integer)
    orderdate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    requireddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    shippeddate: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    freight: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(15, 4))
    shipname: Mapped[Optional[str]] = mapped_column(String(35))
    shipaddress: Mapped[Optional[str]] = mapped_column(String(50))
    shipcity: Mapped[Optional[str]] = mapped_column(String(15))
    shipregion: Mapped[Optional[str]] = mapped_column(String(15))
    shippostalcode: Mapped[Optional[str]] = mapped_column(String(9))
    shipcountry: Mapped[Optional[str]] = mapped_column(String(15))
    shipperid: Mapped[Optional[int]] = mapped_column(Integer)

    customers = relationship("Customers")
    employees = relationship("Employees", back_populates="orders")
    orderDetails = relationship("OrderDetails", back_populates="orders")


class Products(Base):
    __tablename__ = 'products'
    __table_args__ = (
        ForeignKeyConstraint(['categoryid'], ['northwind.categories.categoryid'], name='fk_category'),
        ForeignKeyConstraint(['supplierid'], ['northwind.suppliers.supplierid'], name='fk_supplier'),
        PrimaryKeyConstraint('productid', name='products_pkey'),
        {'schema': 'northwind'}
    )

    productid: Mapped[int] = mapped_column(Integer, primary_key=True)
    supplierid: Mapped[int] = mapped_column(Integer)
    categoryid: Mapped[int] = mapped_column(Integer)
    productname: Mapped[Optional[str]] = mapped_column(String(35))
    quantityperunit: Mapped[Optional[str]] = mapped_column(String(20))
    unitprice: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric(13, 4))
    unitsinstock: Mapped[Optional[int]] = mapped_column(SmallInteger)
    unitsonorder: Mapped[Optional[int]] = mapped_column(SmallInteger)
    reorderlevel: Mapped[Optional[int]] = mapped_column(SmallInteger)
    discontinued: Mapped[Optional[str]] = mapped_column(String(1))
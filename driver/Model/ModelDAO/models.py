from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Identity, Integer, MetaData, Numeric, PrimaryKeyConstraint, SmallInteger, String, Table, Text

metadata = MetaData()


t_categories = Table(
    'categories', metadata,
    Column('categoryid', Integer, primary_key=True),
    Column('categoryname', String(50)),
    Column('description', String(100)),
    PrimaryKeyConstraint('categoryid', name='categories_pkey'),
    schema='northwind'
)

t_customers = Table(
    'customers', metadata,
    Column('customerid', String(5), primary_key=True),
    Column('companyname', String(50)),
    Column('contactname', String(30)),
    Column('contacttitle', String(30)),
    Column('address', String(50)),
    Column('city', String(20)),
    Column('region', String(15)),
    Column('postalcode', String(9)),
    Column('country', String(15)),
    Column('phone', String(17)),
    Column('fax', String(17)),
    PrimaryKeyConstraint('customerid', name='customers_pkey'),
    schema='northwind'
)

t_employees = Table(
    'employees', metadata,
    Column('employeeid', Integer, primary_key=True),
    Column('lastname', String(10)),
    Column('firstname', String(10)),
    Column('title', String(25)),
    Column('titleofcourtesy', String(5)),
    Column('birthdate', DateTime),
    Column('hiredate', DateTime),
    Column('address', String(50)),
    Column('city', String(20)),
    Column('region', String(2)),
    Column('postalcode', String(9)),
    Column('country', String(15)),
    Column('homephone', String(14)),
    Column('extension', String(4)),
    Column('reportsto', Integer),
    Column('notes', Text),
    PrimaryKeyConstraint('employeeid', name='employees_pkey'),
    schema='northwind'
)

t_products = Table(
    'products', metadata,
    Column('productid', Integer, primary_key=True),
    Column('productname', String(35)),
    Column('supplierid', Integer, nullable=False),
    Column('categoryid', Integer, nullable=False),
    Column('quantityperunit', String(20)),
    Column('unitprice', Numeric(13, 4)),
    Column('unitsinstock', SmallInteger),
    Column('unitsonorder', SmallInteger),
    Column('reorderlevel', SmallInteger),
    Column('discontinued', String(1)),
    PrimaryKeyConstraint('productid', name='products_pkey'),
    schema='northwind'
)

t_shippers = Table(
    'shippers', metadata,
    Column('shipperid', Integer, primary_key=True),
    Column('companyname', String(20)),
    Column('phone', String(14)),
    PrimaryKeyConstraint('shipperid', name='shippers_pkey'),
    schema='northwind'
)

t_suppliers = Table(
    'suppliers', metadata,
    Column('supplierid', Integer, primary_key=True),
    Column('companyname', String(50)),
    Column('contactname', String(30)),
    Column('contacttitle', String(30)),
    Column('address', String(50)),
    Column('city', String(20)),
    Column('region', String(15)),
    Column('postalcode', String(8)),
    Column('country', String(15)),
    Column('phone', String(15)),
    Column('fax', String(15)),
    Column('homepage', String(100)),
    PrimaryKeyConstraint('supplierid', name='supplier_pk'),
    schema='northwind'
)

t_orders = Table(
    'orders', metadata,
    Column('orderid', Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True),
    Column('customerid', String(5), nullable=False),
    Column('employeeid', Integer, nullable=False),
    Column('orderdate', DateTime),
    Column('requireddate', DateTime),
    Column('shippeddate', DateTime),
    Column('freight', Numeric(15, 4)),
    Column('shipname', String(35)),
    Column('shipaddress', String(50)),
    Column('shipcity', String(15)),
    Column('shipregion', String(15)),
    Column('shippostalcode', String(9)),
    Column('shipcountry', String(15)),
    Column('shipperid', Integer),
    ForeignKeyConstraint(['customerid'], ['northwind.customers.customerid'], name='fk_orders_customers'),
    ForeignKeyConstraint(['employeeid'], ['northwind.employees.employeeid'], name='fk_orders_employees'),
    PrimaryKeyConstraint('orderid', name='orders_pkey'),
    schema='northwind'
)

t_order_details = Table(
    'order_details', metadata,
    Column('orderid', Integer, primary_key=True, nullable=False),
    Column('productid', Integer, primary_key=True, nullable=False),
    Column('unitprice', Numeric(13, 4)),
    Column('quantity', SmallInteger),
    Column('discount', Numeric(10, 4)),
    ForeignKeyConstraint(['orderid'], ['northwind.orders.orderid'], name='fk_orderdetails_orders'),
    ForeignKeyConstraint(['productid'], ['northwind.products.productid'], name='fk_orderdetails_products'),
    PrimaryKeyConstraint('orderid', 'productid', name='order_details_pkey'),
    schema='northwind'
)

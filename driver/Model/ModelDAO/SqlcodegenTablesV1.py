# Modelagem das Tables do Schema em classes

class Categories:
    def __init__(self, categoryid, categoryname, description):
        self.categoryid = categoryid
        self.categoryname = categoryname
        self.description = description

class Shippers:
    def __init__(self, shipperid, companyname, phone):
        self.shipperid = shipperid
        self.companyname = companyname
        self.phone = phone

class Suppliers:
    def __init__(self, supplierid, companyname, contactname, contacttitle, address, city, region, postalcode, country, phone, fax, homepage):
        self.supplierid = supplierid
        self.companyname = companyname
        self.contactname = contactname
        self.contacttitle = contacttitle
        self.address = address
        self.city = city
        self.region = region
        self.postalcode = postalcode
        self.country = country
        self.phone = phone
        self.fax = fax
        self.homepage = homepage

class Customers:
    def __init__(self, customerid, companyname, contactname, contacttitle, address, city, region, postalcode, country, phone, fax):
        self.customerid = customerid
        self.companyname = companyname
        self.contactname = contactname
        self.contacttitle = contacttitle
        self.address = address
        self.city = city
        self.region = region
        self.postalcode = postalcode
        self.country = country
        self.phone = phone
        self.fax = fax

class Orders:
    def __init__(self, orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid):
        self.orderid = orderid
        self.customerid = customerid
        self.employeeid = employeeid
        self.orderdate = orderdate
        self.requireddate = requireddate
        self.shippeddate = shippeddate
        self.freight = freight
        self.shipname = shipname
        self.shipaddress = shipaddress
        self.shipcity = shipcity
        self.shipregion = shipregion
        self.shippostalcode = shippostalcode
        self.shipcountry = shipcountry
        self.shipperid = shipperid

class Employees:
    def __init__(self, employeeid, lastname, firstname, title, titleofcourtesy, birthdate, hiredate, address, city, region, postalcode, country, homephone, extension, reportsto, notes):
        self.employeeid = employeeid
        self.lastname = lastname
        self.firstname = firstname
        self.title = title
        self.titleofcourtesy = titleofcourtesy
        self.birthdate = birthdate
        self.hiredate = hiredate
        self.address = address
        self.city = city
        self.region = region
        self.postalcode = postalcode
        self.country = country
        self.homephone = homephone
        self.extension = extension
        self.reportsto = reportsto
        self.notes = notes

class Order_details:
    def __init__(self, orderid, productid, unitprice, quantity, discount):
        self.orderid = orderid
        self.productid = productid
        self.unitprice = unitprice
        self.quantity = quantity
        self.discount = discount

class Products:
    def __init__(self, productid, productname, supplierid, categoryid, quantityperunit, unitprice, unitsinstock, unitsonorder, reorderlevel, discontinued):
        self.productid = productid
        self.productname = productname
        self.supplierid = supplierid
        self.categoryid = categoryid
        self.quantityperunit = quantityperunit
        self.unitprice = unitprice
        self.unitsinstock = unitsinstock
        self.unitsonorder = unitsonorder
        self.reorderlevel = reorderlevel
        self.discontinued = discontinued


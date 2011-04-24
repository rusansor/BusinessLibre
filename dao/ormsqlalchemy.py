import sqlalchemy
from sqlalchemy import create_engine

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper

from model.customer import Customer
from model.product import Product

from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()
customers_table = Table('customers', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('cif', String),
)

products_table = Table('products', metadata,
    Column('id', Integer, primary_key=True),
    Column('code', String),
    Column('name', String),
    Column('price', String),
)
mapper(Customer, customers_table)
mapper(Product, products_table)
 
metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

ed_user = Customer(None, 'ed', '44663355')
session.add(ed_user)

session.add_all([
         Customer(None, 'wendy', '3334433388'),
         Customer(None, 'mary', '7755332288'),
         Customer(None, 'fred', '9900119922')])

session.commit()

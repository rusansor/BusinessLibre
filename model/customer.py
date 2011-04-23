from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cif = Column(String)
    
    def __init__(self, name, cif):
        self.name = name
        self.cif = cif

    def __repr__(self):
        return "<Customer('%s','%s'>" % (self.name, self.cif)

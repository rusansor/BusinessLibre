from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

import model.customer

Base = declarative_base()
class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     fullname = Column(String)
     password = Column(String)

     def __init__(self, name, fullname, password):
         self.name = name
         self.fullname = fullname
         self.password = password

     def __repr__(self):
         return "<User('%s','%s', '%s')>" % (self.name, self.fullname, 
self.password)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

ed_user = User('ed', 'Ed Jones', 'edspassword')
session.add(ed_user)

session.add_all([
         User('wendy', 'Wendy Williams', 'foobar'),
         User('mary', 'Mary Contrary', 'xxg527'),
         User('fred', 'Fred Flinstone', 'blah')])

session.commit()

our_user = session.query(User).filter_by(name='ed').first()

print our_user


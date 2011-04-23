from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
class Customer(object):
    
    def __init__(self, name, cif):
        self.name = name
        self.cif = cif

    def __repr__(self):
        return "<Customer('%s','%s'>" % (self.name, self.cif)

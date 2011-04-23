from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
class Customer(object):
    
    def __init__(self, id, name, cif):
        self.id = id
        self.name = name
        self.cif = cif

    def __repr__(self):
        return "<Customer('%s','%s','%s'>" % (self.id, self.name, self.cif)

class Product(object):

    
    def __init__(self, id, code, name, price):
        self.id = id
        self.code = code
        self.name = name
        self.price = price

    def __repr__(self):
        return "<Product('%s','%s','%s','%s'>" % (self.id, self.code, self.name, self.price)

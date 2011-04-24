class Product(object):
<<<<<<< HEAD

=======
    
>>>>>>> product
    def __init__(self, id, code, name, price):
        self.id = id
        self.code = code
        self.name = name
        self.price = price

    def __repr__(self):
<<<<<<< HEAD
        return "<Customer('%s','%s','%s','%s'>" % (self.id, self.code, self.name, self.price)
=======
        return "<Product('%s','%s','%s','%s'>" % (self.id, self.code, self.name, self.price)
>>>>>>> product

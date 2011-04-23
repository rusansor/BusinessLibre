import pygtk
pygtk.require("2.0")
import gtk

class UIControllerCustomer:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("ui/customers.ui")
        self.window = builder.get_object("window_customer_main")

        self.populate_customers_list(builder)
        builder.connect_signals(self)
        self.window.show()

    def populate_customers_list(self, builder):
        self.model = builder.get_object("model")
        self.model.append(['Ruben'])
        self.model.append(['Natalia'])
        print self.model

        for row in self.model:
            value = row[0]
            print value

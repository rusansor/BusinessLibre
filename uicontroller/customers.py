import pygtk
pygtk.require("2.0")
import gtk

from model.customer import Customer

class UIControllerCustomer:
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file("ui/customers.ui")
        self.window = self.builder.get_object("window_customer_main")

        self.populate_customers_list()
        self.builder.connect_signals(self)
        self.window.show()

    def populate_customers_list(self):
        self.model = self.builder.get_object("model")

        ruben = Customer('Ruben','48308895')
        nata = Customer('Natalia','55667769')

        self.model.append([ruben.name])
        self.model.append([nata.name])
        #print self.model

        for row in self.model:
            value = row[0]
            print value

    def on_buttonAdd_clicked(self,widget):
        self.window_edit = self.builder.get_object("window_customer_edit")
        self.window_edit.show()

    def on_buttonApply_clicked(self,widget):
        entryName = self.builder.get_object("entryName")
        name = entryName.get_text()
        entryCIF = self.builder.get_object("entryCIF")
        cif = entryCIF.get_text()
        newCustomer = Customer(name, cif)
        self.addCustomer(newCustomer)

    def addCustomer(self, customer):
        self.model.append([customer.name])



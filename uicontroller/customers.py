import pygtk
pygtk.require("2.0")
import gtk

from dao.ormsqlalchemy import Session
from model.customer import Customer

class UIControllerCustomer:
    def __init__(self):
        self.session = Session()

        self.builder = gtk.Builder()
        self.builder.add_from_file("ui/customers.ui")
        self.window = self.builder.get_object("window_customer_main")
        self.listview = self.builder.get_object("listview")

        self.populate_customers_list()
        self.builder.connect_signals(self)
        self.window.show()

    def populate_customers_list(self):
        self.model = self.builder.get_object("model")
        customers = self.session.query(Customer).all()
        for customer in customers:
            self.model.append([customer.name])

    def on_buttonAdd_clicked(self,widget):
        self.window_edit = self.builder.get_object("window_customer_edit")
        self.window_edit.show()

    def on_buttonEdit_clicked(self,widget):
        print 'editing...'
        self.window_edit = self.builder.get_object("window_customer_edit")
        self.window_edit.show()

    def on_buttonDelete_clicked(self,widget):
        listselection = self.listview.get_selection()
        model, iter = listselection.get_selected()
        data = model.get_value(iter, 0)
        

    def on_buttonApply_clicked(self,widget):
        entryName = self.builder.get_object("entryName")
        name = entryName.get_text()
        entryCIF = self.builder.get_object("entryCIF")
        cif = entryCIF.get_text()
        newCustomer = Customer(name, cif)
        self.addCustomer(newCustomer)

    def addCustomer(self, customer):
        self.model.append([customer.name])



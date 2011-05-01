from gi.repository import Gtk

from dao.ormsqlalchemy import Session
from model.customer import Customer

class UIControllerCustomer:
    def __init__(self):
        self.session = Session()

        self.builder = Gtk.Builder()
        self.builder.add_from_file("ui/customers.ui")
        self.window = self.builder.get_object("window_main")
        self.listview = self.builder.get_object("list_view")
        self.model = self.builder.get_object("list_store")

        self.populate_customers_list()
        self.builder.connect_signals(self)
        self.window.show()

    def populate_customers_list(self):
        self.customers = self.session.query(Customer).all()
        for customer in self.customers:
            self.model.append([customer.id, customer.name, customer.cif])

    def on_buttonAdd_clicked(self,widget):
        self.window_edit = self.builder.get_object("window_customer_edit")
        self.builder.get_object("entryName").set_text('')
        self.builder.get_object("entryCIF").set_text('')

        self.window_edit.show()

    def on_buttonEdit_clicked(self,widget):
        print 'editing...'
        self.window_edit = self.builder.get_object("window_customer_edit")
        self.window_edit.show()

    def on_buttonDelete_clicked(self,widget):
        listselection = self.listview.get_selection()
        model, iter = listselection.get_selected()
        data = model.get_value(iter, 0)
        for customer in self.customers:
            if customer.id == data:
                self.session.delete(customer)
                self.customers.remove(customer)
                self.model.remove(iter)
                self.session.commit()

    def on_buttonApply_clicked(self,widget):
        entryName = self.builder.get_object("entryName")
        name = entryName.get_text()
        entryCIF = self.builder.get_object("entryCIF")
        cif = entryCIF.get_text()
        newCustomer = Customer(None, name, cif)
        self.addCustomer(newCustomer)
        self.window_edit.hide()

    def addCustomer(self, customer):
        self.session.add(customer)
        self.session.commit()
        self.model.append([customer.id, customer.name, customer.cif])



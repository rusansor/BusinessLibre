import pygtk
pygtk.require("2.0")
import gtk

from dao.ormsqlalchemy import Session
from model.product import Product

class UIControllerProducts:
    def __init__(self):
        self.session = Session()

        self.builder = gtk.Builder()
        self.builder.add_from_file("ui/products.ui")
<<<<<<< HEAD
        self.window = self.builder.get_object("window_main")
        self.listview = self.builder.get_object("list_view")
        self.model = self.builder.get_object("list_store")
=======
        self.window = self.builder.get_object("window_product_main")
        self.listview = self.builder.get_object("listview")
        self.model = self.builder.get_object("model")
>>>>>>> product

        self.populate_products_list()
        self.builder.connect_signals(self)
        self.window.show()

    def populate_products_list(self):
        self.model = self.builder.get_object("model")
        self.products = self.session.query(Product).all()
<<<<<<< HEAD
        for product in self.products:
            self.model.append([product.id, product.name, product.cif])
=======
        if self.products is not None:
            for product in self.products:
                self.model.append([product.id, product.name, product.cif])
>>>>>>> product

    def on_buttonAdd_clicked(self,widget):
        self.window_edit = self.builder.get_object("window_product_edit")
        self.window_edit.show()

    def on_buttonEdit_clicked(self,widget):
        print 'editing...'
        self.window_edit = self.builder.get_object("window_product_edit")
        self.window_edit.show()

    def on_buttonDelete_clicked(self,widget):
        listselection = self.listview.get_selection()
        model, iter = listselection.get_selected()
        data = model.get_value(iter, 0)
        for product in self.products:
            if product.id == data:
                self.session.delete(product)
                self.products.remove(product)
                self.model.remove(iter)
                self.session.commit()

    def on_buttonApply_clicked(self,widget):
        entryName = self.builder.get_object("entryName")
        name = entryName.get_text()
        entryCIF = self.builder.get_object("entryCIF")
        cif = entryCIF.get_text()
        newProduct = Product(None, name, cif)
        self.addProduct(newProduct)
        self.window_edit.destroy()

    def addProduct(self, product):
        self.session.add(product)
        self.session.commit()
        self.model.append([product.id, product.name, product.cif])



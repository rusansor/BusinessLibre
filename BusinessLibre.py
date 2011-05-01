#!/usr/bin/python2


from gi.repository import Gtk
from uicontroller.customers import UIControllerCustomer
from uicontroller.products  import UIControllerProducts

import dao.ormsqlalchemy

class App(object):       
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("ui/main.ui")
        self.window = builder.get_object("window")
        self.window.maximize()
        builder.connect_signals(self)
        self.window.show()

    def on_menuitem_customers_activate(self,widget):
        UIControllerCustomer()

    def on_menuitem_products_activate(self,widget):
        UIControllerProducts()

    def on_window_destroy(self, widget, data=None):      
        Gtk.main_quit()

if __name__ == "__main__":
    app = App()
    Gtk.main()


    

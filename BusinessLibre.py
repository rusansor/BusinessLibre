#!/usr/bin/python2


import pygtk
pygtk.require("2.0")
import gtk
from uicontroller.customers import UIControllerCustomer

import main.ormsqlalchemy

class App(object):       
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("ui/main.ui")
        self.window = builder.get_object("window")
        builder.connect_signals(self)
        self.window.show()

    def on_menuitem_customer_activate(self,widget):
        UIControllerCustomer()

    def on_window_destroy(self, widget, data=None):      
        gtk.main_quit()

if __name__ == "__main__":
    app = App()
    gtk.main()


    

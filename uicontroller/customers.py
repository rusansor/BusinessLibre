import pygtk
pygtk.require("2.0")
import gtk

class UIControllerCustomer:
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("ui/customers.ui")
        self.window = builder.get_object("window_customer_main")
        builder.connect_signals(self)
        self.window.show()

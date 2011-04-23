#!/usr/bin/python2

import pygtk
pygtk.require("2.0")
import gtk

class TutorialApp(object):       
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("../../../ui/customers.ui")
        self.window = builder.get_object("window_customer_main")
        self.model = builder.get_object("model")
        self.model.append(['Ruben'])
        self.model.append(['Natalia'])
        print self.model

        for row in self.model:
            value = row[0]
            print value



        builder.connect_signals(self)
        self.window.show()


    def on_window_destroy(self, widget, data=None):      
        print 'bye!!!!!!!!'        
        gtk.main_quit()

if __name__ == "__main__":
    app = TutorialApp()
    gtk.main()


    
#import main.main

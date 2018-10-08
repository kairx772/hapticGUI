#!/usr/bin/env python

from Tkinter import Tk, Frame, Button, Label, Entry
import serial as ser
ser1 = ser.Serial('/dev/ttyUSB0',9600)
#ser1.write('s')

class Example(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.createWidgets()

    def say_hi(self):
        print "hi there, everyone! "
        #print "Name: ", self.name.get()
        #print "Password: ", self.password.get()
        #self.password.delete(0, 'end')

    def say_halo(self):
        print "Moin! Guten Tag! "


    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})
        '''
        # Simple Label widget:
        self.name_title = Label(self, text="Name:")
        self.name_title.pack({"side": "left"})
        
        # Simple Entry widget:
        self.name = Entry(self)
        self.name.pack({"side": "left"})
        self.name.insert(0, "Your name")
        
        # Simple Label widget:
        self.password_title = Label(self, text="Password:")
        self.password_title.pack({"side": "left"})

        # In order to hide the text as it is typed (e.g. for Passwords)
        # set the "show" parameter:
        self.password = Entry(self)
        self.password["show"] = "*"
        self.password.pack({"side": "left"})
        '''
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",

        self.hi_there["command"] = self.say_hi
        self.hi_there.bind("<Enter>", self.on_enter)
        #self.hi_there.bind("<Leave>", self.on_leave)
        self.hi_there.pack({"side": "left"})

        self.guten_tag = Button(self)
        self.guten_tag["text"] = "GutenTag",

        self.guten_tag["command"] = self.say_halo
        #self.hi_there.bind("<Enter>", self.on_enter)
        #self.hi_there.bind("<Leave>", self.on_leave)
        self.guten_tag.pack({"side": "left"})

    def on_enter(self, event):
        print "hi there, hello world! "
        #self.l2.configure(text="Hello world")
        ser1.write('s')

    #def on_leave(self, enter):
        #self.l2.configure(text="")

def main():
    root = Tk()
    app = Example(parent=root)

    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

    app.mainloop()

main()
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
        print "hi there, hello world! "

    def say_halo(self):
        print "Moin! Guten Tag! "

    def createWidgets(self):
        self.master.title("hapticGUI")

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.bind("<Enter>", self.on_enter)
        #self.hi_there.bind("<Leave>", self.on_leave)
        self.hi_there.pack({"side": "left"})

        self.guten_tag = Button(self)
        self.guten_tag["text"] = "GutenTag",
        self.guten_tag["command"] = self.say_halo
        self.guten_tag.pack({"side": "left"})

    def on_enter(self, event):
        print "bzzzzzzzzzz~ "
        ser1.write('s')

    #def on_leave(self, enter):
        #print "bzzzzzzzzzz~ "

def main():
    root = Tk()
    app = Example(parent=root)
    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)
    root.geometry("1200x800")
    app.mainloop()

main()
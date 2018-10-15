#!/usr/bin/env python3
import tkinter as tk
import serial as ser

#ser1 = ser.Serial('/dev/ttyUSB0',9600)
#ser1.write('s')

class MainApplication(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        #self.pack()
        #self.init_window()
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.master.title('hapticmouse_GUI')
        self.master.geometry('1000x1000')
        #self.master.resizable(0, 0)

    def create_widgets(self):
        self.create_buttons()
        self.create_squareframe()

    # Creating the square frame
    def create_squareframe(self):
        self.square_frame = tk.Frame(width=100, height=100, background='red')
        self.square_frame.grid(column=0, row=0)
        self.square_frame.bind("<Enter>", self.on_enter)
        self.square_frame.bind("<Button-2>", self.say_hi)
        self.square_frame.place(x=200, y=200)
        #self.square_frame.pack(expand=True, fill=tk.BOTH)
        #self.left_frame = tk.Frame(width=100, height=100, background='red')
        #self.left_frame.grid_propagate(0)
        #self.square_frame.grid(row=0, column=0)

    def say_hi(self):
        print ('hi there, hello world! ')

    def leftclick(self, event):
        print ('left~ ')

    def on_enter(self, event):
        print ('bzzzzzzzzzz~ ')
        #ser1.write('s')

if __name__ == '__main__':
   root = tk.Tk()
   main_app =  MainApplication(root)
   root.mainloop()
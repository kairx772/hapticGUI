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

        #self.left_frame = tk.Frame(width=100, height=100, background='red')
        #self.left_frame.grid_propagate(0)
        #self.square_frame.grid(row=0, column=0)


    def create_buttons(self):
        self.button1 = tk.Button(text='Button1')
        self.button1.config( height = 5, width = 10 )
        self.button1["command"] = self.say_hi
        self.button1.bind("<Enter>", self.on_enter) 
        self.button1.img = ''
        #self.button1.config(height=100, width=100, image=button1.img, compound=CENTER)      
        self.button1.place(x=600, y=400)


    def say_hi(self):
        print ('hi there, hello world! ')

    def on_enter(self, event):
        print ('bzzzzzzzzzz~ ')
        #ser1.write('s')

if __name__ == '__main__':
   root = tk.Tk()
   main_app =  MainApplication(root)
   root.mainloop()
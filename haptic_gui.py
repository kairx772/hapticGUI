#!/usr/bin/env python3
import tkinter as tk
from tkinter import font  as tkfont
import random
#import serial as ser
#from Xlib import display
import time

# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)

#ser1 = ser.Serial('/dev/ttyUSB1',9600)
#ser1.write(str.encode('s'))

class Data:
    def __init__(self):
        self.startime = 0
        self.endtime = 0
        self.cur_posx = 0
        self.cur_posy = 0
        self.sq_posx = 0
        self.sq_posy = 0
        self.sq_wid = 0



data = Data()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        #self.geometry('1000x800')
        pad = 0
        self.overrideredirect(1)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth()-pad, self.winfo_screenheight()-pad))

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", expand=True)
        #container.grid_rowconfigure(0, weight=0)
        #container.grid_columnconfigure(0, weight=0)

        self.frames = {}
        for F in (StartPage, PageTwo):
            page_name = F.__name__
            print (F)
            print(type(F))
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.square = []
        label = tk.Label(self, text="Click the red square, and press the button to remake it.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button2 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button4 = tk.Button(self, text=" ",
                           command=lambda: self.creatthis())
        #button4.place(relx=.5, rely=.5)    
        self.create_squareframe()

        button2.pack()
        button4.pack()
    def create_squareframe(self):
        targetsize = random.randint(15,150)
        #targetsize = 20
        x_pos = random.randint(0,1910 - 65 -targetsize)
        y_pos = random.randint(0,1070- 25 - targetsize)
        #x_pos = 1920  - targetsize
        #y_pos = 1080 - targetsize
        self.square_frame = tk.Frame(width=targetsize, height=targetsize, background='red')
        #self.square_frame.grid(column=0, row=0)
        self.square_frame.bind("<Enter>", self.on_enter)
        self.square_frame.bind("<Button-1>", lambda x:self.removethis_sq())
        self.square_frame.place(x = x_pos, y = y_pos)
        #self.square_frame.configure(background="blue")
        #self.square_frame.destroy()
    def on_enter(self, event):
        print ('bzzzzzzzzzz~ ')
        #ser1.write(str.encode('s'))
        #ser1.write('s')
    def removethis(self):
        self.square_frame.destroy()
    def removethis_sq(self):
        self.square_frame.configure(background="blue")
        data.endtime = time.time()
        print(data.endtime - data.startime)
    def creatthis(self):
        data.startime = time.time()
        self.square_frame.destroy()
        self.create_squareframe()

if __name__ == "__main__":
    app = SampleApp()
    #sf = SquareFrame()
    app.mainloop()
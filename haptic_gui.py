#!/usr/bin/env python3
import tkinter as tk
from tkinter import font  as tkfont
from random import randint, choice
#import serial as ser
#from Xlib import display
import time
import pyautogui



# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)

#ser1 = ser.Serial('/dev/ttyUSB1',9600)
#ser1.write(str.encode('s'))

class Data:
    def __init__(self):
        self.movtime = 0
        self.cur_posx = 0
        self.cur_posy = 0
        self.sq_posx = 0
        self.sq_posy = 0
        self.sq_wid = 0



data = Data()
datalist = []




class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.geometry('1000x800')
        pad = 0
        self.overrideredirect(1)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth()-pad, self.winfo_screenheight()-pad))

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        #container.pack()
        container.pack(side="top", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

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
        self.create_squareframe()
        self.create_quit()
        self.create_savedata()
        self.controller = controller
        self.square = []
        label = tk.Label(self, text="Click the red square, and press the button to remake it.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #button2 = tk.Button(self, text="Go to the start page",
                           #command=lambda: self.backtostartframe())
        button4 = tk.Button(self, text=" ",
                           command=lambda: self.creatthis())


        #button2.pack(side="top", anchor="ne", expand=True)
        button4.pack()
    def create_squareframe(self):
        targetsize = randint(15,150)
        global tar_size
        tar_size = targetsize
        #targetsize = 20
        #x_pos = randint(0,1920 - targetsize)
        #y_pos = randint(0,1080- 25 - targetsize)
        x_pos = (choice([randint(0,945-targetsize),randint(975,1920)]))
        y_pos = (choice([randint(0,555-targetsize),randint(580,1080)]))
        global tarpos_x
        global tarpos_y
        tarpos_x = x_pos + (targetsize/2)
        tarpos_y = y_pos + (targetsize/2)
        #x_pos = 1920  - targetsize
        #y_pos = 1080 - targetsize
        self.square_frame = tk.Frame(width=targetsize, height=targetsize, background='red')
        #self.square_frame.grid(column=0, row=0)
        self.square_frame.bind("<Enter>", self.on_enter)
        self.square_frame.bind("<Button-1>", lambda x:self.removethis_sq())
        self.square_frame.place(x = x_pos, y = y_pos)
        #self.square_frame.configure(background="blue")
        #self.square_frame.destroy()
    def create_quit(self):
        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack(side="top", anchor="nw", expand=True)
    def create_savedata(self):
        self.save = tk.Button(self)
        self.save["text"] = "SAVE"
        self.save["fg"]   = "blue"
        self.save["command"] =  lambda: self.backtostartframe()
        self.save.pack(side="bottom", anchor="se", expand=True)
        #self.QUIT.pack()
    def on_enter(self, event):
        print ('bzzzzzzzzzz~ ')
        #ser1.write(str.encode('s'))
        #ser1.write('s')
    def removethis(self):
        self.square_frame.destroy()
    def removethis_sq(self):
        self.square_frame.configure(background="blue")
        endtime = time.time()
        print('end')
        print ('startime:', startime)
        #print(endtime)
        tataltime = (time.time() - startime)
        print ('tataltime', tataltime)
        #print(endtime - 1000)
        datalist.append(Data())
        datalist[-1].movtime = tataltime
        #print ('tarpx',tarpos_x)
        datalist[-1].sq_posx = tarpos_x
        datalist[-1].sq_posy = tarpos_y
        datalist[-1].sq_wid = tar_size
        print ('movtime:', datalist[-1].movtime, 'sq_posx:', datalist[-1].sq_posx, 'sq_posy:', datalist[-1].sq_posy, 'sq_wid:', datalist[-1].sq_wid)
    def creatthis(self):
        #pyautogui.position()
        print ('x:', pyautogui.position()[0], 'y:', pyautogui.position()[1])
        global startime
        startime = time.time()
        print ('start')
        print (startime)
        self.square_frame.destroy()
        self.create_squareframe()
    def backtostartframe(self):
        #controller.show_frame("StartPage")
        for i in datalist:
            print ('movtime:', i.movtime, 'sq_posx:', i.sq_posx, 'sq_posy:', i.sq_posy, 'sq_wid:', i.sq_wid)

if __name__ == "__main__":
    app = SampleApp()
    #sf = SquareFrame()
    app.mainloop()
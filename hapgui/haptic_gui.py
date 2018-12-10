#!/usr/bin/env python3
import tkinter as tk
from tkinter import font  as tkfont
from random import randint, choice
import serial as ser
import time
import pyautogui
import csv
import pandas as pd

try:
    ser1 = ser.Serial('/dev/ttyUSB0',115200)
except ser.serialutil.SerialException:
    print('Arduino disconnect')

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

#baredgex = 65
#baredgey = 24
baredgex = 0
baredgey = 0


def GenCSV(datalsit, exporfoldername):
    with open(exporfoldername+'.ods', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['movtime', 'cur_posx','cur_posy' ,'sq_posx', 'sq_posy', 'sq_wid'])
        for i in datalsit:
            writer.writerow([str(i.movtime), str(i.cur_posx), str(i.cur_posy), str(i.sq_posx), str(i.sq_posy), str(i.sq_wid)])


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.geometry('1000x800')
        pad = 0
        #self.overrideredirect(True)
        self.attributes('-fullscreen', True)
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
        label = tk.Label(self, text="Save your name and press 'START'", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.entry = tk.Entry(self)
        self.entry.pack()
        testername = self.entry.get()
        button = tk.Button(self, text="Save name", command=self.on_button)
        #button2 = tk.Button(self, text="save name", command=lambda: testername = self.entry.get())
        button1 = tk.Button(self, text="START",
                            command=lambda: controller.show_frame("PageTwo"))
        button.pack()
        button1.pack()

    def on_button(self):
        global testername
        testername = self.entry.get()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.create_squareframe()
        self.create_quit()
        self.create_savedata()
        self.controller = controller
        self.square = []
        global datalist
        #global var
        #var.set(len(datalist))
        #trl = tk.Label(self, text = "trail number = ")
        #trl.pack()
        #trlnum = tk.Label(self, textvariable = var)
        #trlnum.pack(side="top", anchor="w", fill="x", expand="yes")
        label = tk.Label(self, text="Click the red square, and press the button to remake it.", font=("Helvetica", 14))
        label.pack(side="top", fill="x", pady=10)
        #button2 = tk.Button(self, text="Go to the start page",
                           #command=lambda: self.backtostartframe())
        button4 = tk.Button(self, text=" ",
                           command=lambda: self.creatthis())


        #button2.pack(side="top", anchor="ne", expand=True)
        button4.pack()
    def create_squareframe(self):
        targetsize = randint(15,150)
        #targetsize = 1
        global tar_size
        tar_size = targetsize
        #targetsize = 20
        #x_pos = randint(0,1920 - targetsize)
        #y_pos = randint(0,1080- 25 - targetsize)
        x_pos = (choice([randint(0,913-targetsize-baredgex),randint(945,1920-targetsize-baredgex)]))
        y_pos = (choice([randint(0,548-targetsize),randint(570,1080-targetsize-baredgey)]))
        #x_pos = 1920-targetsize-65
        #y_pos = 1080-targetsize-24
        global tarpos_x
        global tarpos_y
        tarpos_x = x_pos + (targetsize/2)
        tarpos_y = y_pos + (targetsize/2)
        #x_pos = 1920 - targetsize
        #y_pos = 1080 - targetsize
        self.square_frame = tk.Frame(width=targetsize, height=targetsize, background='red')
        #self.square_frame.grid(column=0, row=0)
        self.square_frame.bind("<Enter>", self.on_enter)
        self.square_frame.bind("<Leave>", self.on_leave)
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
        try:
            ser1.write(str.encode('s'))
        except NameError:
            print ('bzzzzzzzzzz~ ')
    def on_leave(self, event):
        try:
            ser1.write(str.encode('q'))
        except NameError:
            print ('mmmmmmmmmmmmmm~ ')
    def removethis(self):
        self.square_frame.destroy()
    def removethis_sq(self):
        try:
            ser1.write(str.encode('q'))
        except NameError:
            print ('mmmmmmmmmmmmmm~ ')
        #print (pyautogui.position())
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
        datalist[-1].cur_posx = cur_starx - baredgex
        datalist[-1].cur_posy = cur_stary - baredgey
        # print ('movtime:', datalist[-1].movtime, 
        #     'sq_posx:', datalist[-1].sq_posx, 
        #     'sq_posy:', datalist[-1].sq_posy, 
        #     'sq_wid:', datalist[-1].sq_wid, 
        #     'cur_posx:', datalist[-1].cur_posx,
        #     'cur_posy:', datalist[-1].cur_posy)
    def creatthis(self):
        #print ('x:', pyautogui.position()[0], 'y:', pyautogui.position()[1])
        global cur_starx
        global cur_stary
        global startime
        startime = time.time()
        (cur_starx, cur_stary) = pyautogui.position()
        print (pyautogui.position())
        print ('start')
        print (startime)
        self.square_frame.destroy()
        self.create_squareframe()
    def backtostartframe(self):
        #controller.show_frame("StartPage")
        GenCSV(datalist, testername)
        # for i in datalist:
        #     print ('movtime:', i.movtime, 'sq_posx:', i.sq_posx, 'sq_posy:', i.sq_posy, 'sq_wid:', i.sq_wid)

if __name__ == "__main__":
    app = SampleApp()
    #sf = SquareFrame()
    app.mainloop()
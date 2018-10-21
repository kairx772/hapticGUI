#!/usr/bin/env python3
import tkinter as tk
from tkinter import font  as tkfont
import random

#ser1 = ser.Serial('/dev/ttyUSB0',9600)
#ser1.write('s')





class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry('1000x800')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
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

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Destroy",
                            command=lambda: square_frame.destroy(self))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to the page2",
                           command=lambda: controller.show_frame("PageTwo"))
        button2 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        self.create_squareframe()
        button1.pack()
        button2.pack()


    def create_squareframe(self):
        targetsize = random.randint(5,100)
        self.square_frame = tk.Frame(width=targetsize, height=targetsize, background='red')
        #self.square_frame.grid(column=0, row=0)
        self.square_frame.bind("<Enter>", self.on_enter)
        self.square_frame.bind("<Button-1>", lambda: controller.show_frame("PageTwo"))
        self.square_frame.place(x=random.randint(30,450), y=random.randint(30,500))

    def on_enter(self, event):
        print ('bzzzzzzzzzz~ ')
        #ser1.write('s')

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to the page1",
                           command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))        
        self.create_squareframe()
        create_squareframe_fn(self)
        button1.pack()
        button2.pack()
    def create_squareframe(self):
        targetsize = random.randint(5,100)
        self.square_frame = tk.Frame(width=targetsize, height=targetsize, background='red')
        #self.square_frame.grid(column=0, row=0)
        self.square_frame.bind("<Enter>", self.on_enter)
        self.square_frame.bind("<Button-1>", lambda: controller.show_frame("PageTwo"))
        self.square_frame.place(x=random.randint(30,450), y=random.randint(30,500))

    def on_enter(self, event):
        print ('bzzzzzzzzzz~ ')
        #ser1.write('s')


def create_squareframe_fn(self):
    targetsize = random.randint(5,100)
    square_frame = tk.Frame(width=targetsize, height=targetsize, background='green')
        #self.square_frame.grid(column=0, row=0)
    square_frame.bind("<Enter>", on_enter_fn())
        #self.square_frame.bind("<Button-1>", lambda: controller.show_frame("PageTwo"))
    square_frame.place(x=random.randint(30,450), y=random.randint(30,500))

def on_enter_fn():
    print ('bzzzzzzzzzzlalalalallalal~ ')
    #ser1.write('s')

'''
class SquareFrame(tk.Tk):

    def __init__(self):
        targetsize = random.randint(5,100)
        tk.Frame.__init__(self, width=targetsize, height=targetsize, background='green')
        self.place(x=random.randint(30,450), y=random.randint(30,500))
        #self.controller = controller
        #label = tk.Label(self, text="This is page 1", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
        #button1 = tk.Button(self, text="Go to the page2",
                           #command=lambda: controller.show_frame("PageTwo"))
        #button2 = tk.Button(self, text="Go to the start page",
                           #command=lambda: controller.show_frame("StartPage"))
        #self.create_squareframe()
        #button1.pack()
        #button2.pack()
'''
'''

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
        temp1 = self.create_squareframe()
        self.create_button()
        #print (type(temp1))

    def create_button(self):
        self.erase = tk.Button(root,text='Clear',command=clear).grid(row=1)

    # Creating the square frame
    def create_squareframe(self):
        targetsize = random.randint(5,100)
        self.square_frame = tk.Frame(width=targetsize, height=targetsize, background='red')
        self.square_frame.grid(column=0, row=0)
        self.square_frame.bind("<Enter>", self.on_enter)
        self.square_frame.bind("<Button-1>", self.check_info)
        self.square_frame.place(x=random.randint(30,450), y=random.randint(30,500))
        #self.square_frame.pack(expand=True, fill=tk.BOTH)
        #self.left_frame = tk.Frame(width=100, height=100, background='red')
        #self.left_frame.grid_propagate(0)
        #self.square_frame.grid(row=0, column=0)
        #我在衝三小朋友?

    def check_info(self, event):
        targetsize = random.randint(5,100)
        self.square_frame = tk.Frame(width=targetsize, height=targetsize, background='red')
        self.square_frame.grid(column=0, row=0)
        self.square_frame.bind("<Enter>", self.on_enter)
        self.square_frame.bind("<Button-1>", self.check_info)
        #self.square_frame.bind("<Button-1>", print ('click click~'))
        #self.square_frame.bind("<Button-1>", lambda x:self._close())
        self.square_frame.place(x=random.randint(0,1000), y=random.randint(0,1000))


        def close(self):
            self.square_frame.destroy()
        #self.resizable(False, False)

        #ttk.Button(self.info_frame, text="Return Home", command=self.goback).grid(column=2, row=2, sticky=(W, E))
    def _close(self):
        self.destroy()

    def clear(self):
        list = root.grid_slaves()
        for l in list:
            print (type(l))
            l.destroy()

    def goback(self):
        self.info_frame.destroy()

    def say_hi(self):
        print ('hi there, hello world! ')

    def leftclick(self, event):
        print ('left~ ')

    def on_enter(self, event):
        print ('bzzzzzzzzzz~ ')
        #ser1.write('s')

'''

'''
if __name__ == '__main__':
   root = tk.Tk()
   main_app =  MainApplication(root)
   root.mainloop()
'''

if __name__ == "__main__":
    app = SampleApp()
    #sf = SquareFrame()
    app.mainloop()
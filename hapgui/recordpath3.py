import struct
import serial as ser
import time
import pandas as pd
import numpy as np
import pyautogui
import threading
from time import sleep

'''
ser1 = ser.Serial('/dev/ttyUSB0',115200)
ser1.write(str.encode('s'))
'''

#file = open( "/dev/input/mice", "rb" );
class mouevt():

    def __init__(self):
        self.button = 0
        self.bLeft = 0
        self.bMiddle = 0
        self.bRight = 0
        self.vxy = (0,0)
        self.pixxy = (0,0)
        self.tmark = 0.0


class getMouEvt():

    def __init__(self, mouevtfile):
        # threading.Thread.__init__(self)
        # self.threadID = threadID
        # self.name = name
        # self.counter = counter
        ft = time.time() 
        self.file = mouevtfile #open( "/dev/input/mice", "rb" )
        print ("sttime: %f" %(time.time()-ft))
        self.evtn = 0
        self.evtque = [None]*10
        self.L = []
        self.M = []
        self.R = []
        self.vx = []
        self.vy = []
        self.tmou = []
        self.cur_x = []
        self.cur_y = []
        self.stmark = time.time()
        #self.tmark = time.time()
        self.distcount = 0
        self.curevt = pd.DataFrame()
    def getMouseEvent(self):
        self.buf = self.file.read(3);
        self.mevt = mouevt()
        self.button = self.buf[0];
        self.mevt.bLeft = self.button & 0x1;
        self.mevt.bMiddle = ( self.button & 0x4 ) > 0;
        self.mevt.bRight = ( self.button & 0x2 ) > 0;
        self.mevt.vxy = struct.unpack( "bb", self.buf[1:] )
        self.mevt.pixxy = pyautogui.position()
        self.mevt.tmark = time.time() - self.stmark
        self.evtn = self.evtn+1
        #print (self.buf)
        #print ("L:%d, M: %d, R: %d, x: %d, y: %d n: %d" % (self.mevt.bLeft,self.mevt.bMiddle,self.mevt.bRight, self.mevt.vxy[0], self.mevt.vxy[1], self.evtn) );
        #print ("pix_x:%d, pix_x:%d, time:%f\n" % (self.mevt.pixxy[0], self.mevt.pixxy[1], self.mevt.tmark))

        self.evtque.insert(0, self.mevt)
        self.evtque.pop(-1)
        #print (self.evtque)
        print (self.evtn)
        #print ("\n")

        self.L.append(self.mevt.bLeft)
        self.M.append(self.mevt.bMiddle)
        self.R.append(self.mevt.bRight)
        self.vx.append(self.mevt.vxy[0])
        self.vy.append(self.mevt.vxy[1])
        self.tmou.append(self.mevt.tmark)
        self.cur_x.append(self.mevt.pixxy[0])
        self.cur_y.append(self.mevt.pixxy[1])

        try:
            ser1.write(str.encode('d'))
        except NameError:
            print ('Send "d" to serial')

class Counter(object):

    def __init__(self, name, mouevtfile):
        self.name = name
        self.number = 0
        self.running = False
        self.file = mouevtfile

    def start(self):
        gmd = getMouEvt(self.file)
        mouevtdata = pd.DataFrame()
        self.running = True
        datalist = []
        while self.running:
            gmd.getMouseEvent()
            #print (gmd.evtque[0].pixxy)
        #print (gmd.L)
        mouevtdata['L'] = list(gmd.L)
        mouevtdata['M'] = gmd.M
        mouevtdata['R'] = gmd.R
        mouevtdata['x'] = gmd.vx
        mouevtdata['y'] = gmd.vy
        mouevtdata['time'] = gmd.tmou
        mouevtdata['cur_x'] = gmd.cur_x
        mouevtdata['cur_y'] = gmd.cur_y
        mouevtdata.to_csv(self.name+'.ods', index=False)


    def status(self):
        return self.number

    def stop(self):
        self.running = False

class Cmd(object):
    t = None
    counter = None
    def __init__(self, name, mouevtfile):
        self.name = name
        self.file = mouevtfile
 
    def start(self):
        self.counter = Counter(self.name, self.file)
        self.t = threading.Thread(target=self.counter.start)
        self.t.start()

    def do_status(self):
        return self.counter.status()

    def stop(self):
        self.counter.stop()
        # waiting while thread with Counter will finish
        self.t.join()


if __name__ == "__main__":
    try:
        ser1 = ser.Serial('/dev/ttyUSB2',115200)
    except ser.serialutil.SerialException:
        print('Arduino disconnect')

    file = open( "/dev/input/mice", "rb" ) 
    cmd = Cmd('test', file)
    print ("Starting")
    cmd.start()
    sleep(3)
    print (cmd.do_status())
    sleep(1)
    print (cmd.do_status())
    cmd.stop()
    print ("Count")

import serial as ser
ser1 = ser.Serial('/dev/ttyUSB1',9600)
ser1.write(str.encode('s'))

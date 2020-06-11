import time, serial, pyfirmata, sys
# import tkinter as tk
# from tkinter import *
pinG = 10
pinY = 11
pinR = 12

strComPort = '/dev/ttyACM0'
strComBaud = 9600

brdUno = pyfirmata.Arduino(strComPort)

brdUno.digital[pinY].write(0)
brdUno.digital[pinR].write(0)
brdUno.digital[pinG].write(1)
time.sleep(3)
brdUno.digital[pinG].write(0)
brdUno.digital[pinY].write(1)
time.sleep(3)
brdUno.digital[pinY].write(0)
brdUno.digital[pinR].write(1)
time.sleep(3)
brdUno.digital[pinR].write(0)
print("HOLA")
brdUno.exit()
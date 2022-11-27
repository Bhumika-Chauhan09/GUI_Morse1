from tkinter import*
import tkinter.font 
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM) 
import time

## hardware
Led = LED (14)

## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font. Font(family = 'Helvetica', size = 12, weight = "bold")
translate_dict = { 'A':'.-', 
                   'B':'-...',
                    'C':'-.-.', 
                    'D':'-..', 
                    'E':'.',
                    'F':'..-.', 
                    'G':'--.', 
                    'H':'....',
                    'I':'..', 
                    'J':'.---',
                     'K':'-.-',
                    'L':'.-..',
                     'M':'--', 
                     'N':'-.',
                    'O':'---',
                     'P':'.--.', 
                     'Q':'--.-',
                    'R':'.-.',
                     'S':'...', 
                     'T':'-',
                    'U':'..-', 
                    'V':'...-',
                     'W':'.--',
                    'X':'-..-', 
                    'Y':'-.--', 
                    'Z':'--..',
                    '1':'.----', 
                    '2':'..---', 
                    '3':'...--',
                    '4':'....-', 
                    '5':'.....', 
                    '6':'-....',
                    '7':'--...', 
                    '8':'---..', 
                    '9':'----.',
                    '0':'-----', 
                    ', ':'--..--', 
                    '.':'.-.-.-',
                    '?':'..--..', 
                    '/':'-..-.', 
                    '-':'-....-',
                    '(':'-.--.',
                     ')':'-.--.-'}
ledinput = str()

### EVENT FUNCTIONS ###


def dash():
    Led.on()
    time.sleep(0.6)
    Led.off()
    time.sleep(0.3)
def dot():
    Led.on()
    time.sleep(0.2)
    Led.off()
    time.sleep(0.1)
    
def Morse_code(ledinput):
    ledinput = code.get()
    ledinput = " ".join(translate_dict[c] for c in ledinput.upper())
    print(ledinput)
    for c in ledinput:
        if c == ".":
            dot()
        elif c == "-":
            dash()
        elif c == "/" or c == " ":
            time.sleep(0.5)
        else:
            print("Enter a valid Character")
            
##this method is to destroy the window ans set the pins to initilal
def close():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###
ledButton = Button (win, text = 'Blink Name', font = myFont, command = lambda: Morse_code(ledinput), bg = 'orange', height = 1)
ledButton.grid (row=0, column=1)

code = Entry(win, font=myFont, width=10)
code.grid(row=0, column=0)

exitButton = Button (win, text = 'Exit', font = myFont, command = close, bg = 'aqua', height = 1, width = 6)
exitButton.grid (row=2, column=1)

win.protocol("WM_DELETE_WINDOW", close) # exit cleanly

win.mainloop() # Loop forever
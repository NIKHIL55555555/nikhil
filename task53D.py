from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
from tkinter import ttk
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

win = Tk()
win.title("MORSE CODE BLINKING")

redled = LED(18)

variable= Entry(win, width = 40, bg = "blue", fg = "white")
variable.focus_set()
variable.pack()

def dash():
    redled.on()
    time.sleep(2.0)
    redled.off()
    time.sleep(0.25)

def dot():
    redled.on()
    time.sleep(0.75)
    redled.off()
    time.sleep(0.25)

def nameconverter():
    name = variable.get()
    text = name.upper()
    if len(name) < 13:
        i=0
        while i < (len(name)):
            if text[i] == 'A':
                dot()
                dash()
            if text[i] == 'B':
                dash()
                dot()
                dot()
                dot()
            if text[i] == 'C':
                dash()
                dot()
                dash() 
                dot()
            if text[i] == 'D':
                dash()
                dot() 
                dot()
            if text[i] == 'E':
                dot()
            if text[i] == 'F':
                dot() 
                dot() 
                dash() 
                dot()
            if text[i] == 'G':
                dash() 
                dash() 
                dot()
            if text[i] == 'H':
                dot() 
                dot() 
                dot()
                dot()
            if text[i] == 'I':
                dot()
                dot()
            if text[i] == 'J':
                dot()
                dash() 
                dash()
                dash()
            if text[i] == 'K':
                dash()
                dot() 
                dash()
            if text[i] == 'L':
                dot() 
                dash() 
                dot()
                dot()
            if text[i] == 'M':
                dash() 
                dash()
            if text[i] == 'N':
                dash() 
                dot()
            if text[i] == 'O':
                dash() 
                dash() 
                dash()
            if text[i] == 'P':
                dot() 
                dash() 
                dash()
                dot()
            if text[i] == 'Q':
                dash() 
                dash() 
                dot() 
                dash()
            if text[i] == 'R':
                dot() 
                dash() 
                dot()
            if text[i] == 'S':
                dot() 
                dot() 
                dot()
            if text[i] == 'T':
                dash()
            if text[i] == 'U':
                dot() 
                dot() 
                dash()
            if text[i] == 'V':
                dot() 
                dot() 
                dot() 
                dash()
            if text[i] == 'W':
                dot()
                dash() 
                dash()
            if text[i] == 'X':
                dash() 
                dot() 
                dot() 
                dash()
            if text[i] == 'Y':
                dash() 
                dot() 
                dash() 
                dash()
            if text[i] == 'Z':
                dash() 
                dash() 
                dot() 
                dot() 
            if text[i] == ' ':
                time.sleep(2)
            i = i + 1
    else:
        print("ENTER YOUR TEXT LESS THAN 12 WORDS")


def close():
    RPi.GPIO.cleanup()
    win.destroy()


submitbutton = Button(win, text = "SUBMIT", command = nameconverter, bg = "yellow", fg = "black")
submitbutton.pack()

exitbutton = Button(win, text = "EXIT", command = close, bg = "Red", fg = "black")
exitbutton.pack()

win.mainloop()

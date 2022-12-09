from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
from tkinter import ttk
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

win = Tk()      // open gui window
win.title("MORSE CODE BLINKING")  // set window title

redled = LED(18)   // set the variable of the red led

variable= Entry(win, width = 40, bg = "blue", fg = "white") // customizing the opened window set background color, width
variable.focus_set()
variable.pack()

def dash():              // creating a function
    redled.on()          //turn the led on 
    time.sleep(2.0)      // delay of 200 milli second
    redled.off()         //turn the led off 
    time.sleep(0.25)     // delay of 25 milli second

def dot():
    redled.on()          //turn the led on 
    time.sleep(0.75)     // delay of 75 milli second
    redled.off()         //turn the led off
    time.sleep(0.25)     // delay of 25 milli second

def nameconverter():         // created function
    name = variable.get()    // getting the user input
    text = name.upper()      // set input in capital letter
    if len(name) < 13:       // set the length of the input to 13
        i=0
        while i < (len(name)):      // initilizing the functions according to the morse code     
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
        print("ENTER YOUR TEXT LESS THAN 12 WORDS")      // if the input is gretear than 13 


def close():       // created function
    RPi.GPIO.cleanup()     // close the poped window
    win.destroy()


submitbutton = Button(win, text = "SUBMIT", command = nameconverter, bg = "yellow", fg = "black")   // created a submit button in gui 
submitbutton.pack()

exitbutton = Button(win, text = "EXIT", command = close, bg = "Red", fg = "black")  // for exiting from the window
exitbutton.pack()

win.mainloop()

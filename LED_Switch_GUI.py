# GPIO.setwarnings(False) to disable GPIO warnings
# GPIO.setmode(GPIO.BOARD) # Locate pins by numerical order (Number in the middle of the diagram)
# GPIO.setmode(GPIO.BCM) # Locate pins by Broadcom SOC Channel (Number on the sides of the diagram)
# GPIO.setup(Pin,OUT/IN) # Set pin to output or input

pin = 23 # Set var "pin" to int 23
import RPi.GPIO as GPIO # Required to control GPIO pins on the Raspberry Pi
from tkinter import * # tkinter is a graphical user interface for python
from tkinter import messagebox # messagebox allows tkinter to display notification windows
GPIO.setwarnings(False) # Disable GPIO warnings
GPIO.setmode(GPIO.BCM) # Locate pins by Broadcom SOC Channel (Number on the sides of the diagram)
GPIO.setup(pin,GPIO.OUT) # Set pin to output (Pin, OUT/IN)

def led_switch ():
    if GPIO.input(pin): # If LED is on
        GPIO.output(pin,GPIO.LOW) # Turn off
        msg = messagebox.showinfo( "LED Switch", "OFF")

    else: # Otherwise
        GPIO.output(pin,GPIO.HIGH) # Turn on
        msg = messagebox.showinfo( "LED Switch", "ON")
        
root = Tk() # Sets root var as tkinter and calls tkinter function
root.geometry("100x100") # Sets the height and width of tkinter window
A = Button(top, text = "Led Switch", command = led_switch) # Sets A var as a pre-configured button
A.place(x = 0,y = 0) # Places the button at the top left of the window
root.mainloop() # Calls tkinter mainloop function to open tkinter window

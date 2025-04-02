#!python3
"""
We start by importing a module, and also import all of the important
code from that module. I'm not sure why they do it this way, but 
that's the way it is.
"""
import tkinter as tk 
from tkinter import *

from tkinter import ttk


"""
We create an object using some of the built in functions from the
tkinter Tk class. We also use some of the object methods to set
some of the properties of the window.
"""
window = tk.Tk()
window.title("Packing Widgets example")


"""
A window actually has an infinite running while loop while
it checks to see if any of the features of the window (buttons,
text entry, etc) are being mainpulated.  These features are also
called WIDGETS, and we'll see how they can be added in the next few
files.
"""







entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=34)
lable3 = tk.Label(window, text="X")
entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=35)


#checkbutton options can be found at http://effbot.org/tkinterbook/checkbutton.htm
check1 = tk.Checkbutton(window)






entry1.pack()
lable3.pack()
entry2.pack()

#--------------------------------------------------------------------------
# A Frame can be used to help organize how you want your widgets placed:
# A Frame acts like a single widget, into which you can put other widgets
# We can now position multiple frames in a row by adjusting the "side"
# when we pack() it.
nF = Frame()

nF.pack()



window.mainloop()
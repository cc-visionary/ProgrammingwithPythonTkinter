"""
This is just a dice program that I made where you press the button roll, and it virtually rolls and gives you a side of the dice.
It can only be rolled once though and that's it. I don't know how to like reset the command to roll the dice again. 

@author : Potterishpotter 04/05/2018
"""

from tkinter import *
from tkinter import ttk
from random import randint

def default(*args):
    ttk.Label(dice, text='   ').grid(column=0, row=0, columnspan=3)
    ttk.Label(dice, text='   ').grid(column=0, row=1, columnspan=3)
    ttk.Label(dice, text='   ').grid(column=0, row=2, columnspan=3)

root = Tk()

dice = ttk.Frame(root, padding='5 5 5 5', width=5, height=3, borderwidth=1, relief='raised')

#==============================================FUNCTIONS===================================================================
def removePrev(*args):                                        # removes the previous existing widgets in the frame 'dice'
    for child in dice.winfo_children():
        child.destroy()

def one(*args):
    removePrev()
    ttk.Label(dice, text='   ').grid(column=0, row=0, columnspan=3)
    ttk.Label(dice, text=' ').grid(column=0, row=1)
    ttk.Label(dice, text='O').grid(column=1, row=1)
    ttk.Label(dice, text=' ').grid(column=2, row=1)
    ttk.Label(dice, text='   ').grid(column=0, row=2, columnspan=3)

def two(*args):
    removePrev()
    ttk.Label(dice, text='   ').grid(column=0, row=0, columnspan=3)
    ttk.Label(dice, text='O').grid(column=0, row=1)
    ttk.Label(dice, text=' ').grid(column=1, row=1)
    ttk.Label(dice, text='O').grid(column=2, row=1)
    ttk.Label(dice, text='   ').grid(column=0, row=2, columnspan=3)

def three(*args):
    removePrev()
    ttk.Label(dice, text='O').grid(column=0, row=0)
    ttk.Label(dice, text=' ').grid(column=1, row=0, columnspan=2)
    ttk.Label(dice, text=' ').grid(column=0, row=1)
    ttk.Label(dice, text='O').grid(column=1, row=1)
    ttk.Label(dice, text=' ').grid(column=2, row=1)
    ttk.Label(dice, text='  ').grid(column=0, row=2, columnspan=2)
    ttk.Label(dice, text='O').grid(column=2, row=2)

def four(*args):
    removePrev()
    ttk.Label(dice, text='O').grid(column=0, row=0)
    ttk.Label(dice, text=' ').grid(column=1, row=0)
    ttk.Label(dice, text='O').grid(column=2, row=0)
    ttk.Label(dice, text='   ').grid(column=0, row=1, columnspan=3)
    ttk.Label(dice, text='O').grid(column=0, row=2)
    ttk.Label(dice, text=' ').grid(column=1, row=2)
    ttk.Label(dice, text='O').grid(column=2, row=2)

def five(*args):
    removePrev()
    ttk.Label(dice, text='O').grid(column=0, row=0)
    ttk.Label(dice, text=' ').grid(column=1, row=0)
    ttk.Label(dice, text='O').grid(column=2, row=0)
    ttk.Label(dice, text=' ').grid(column=0, row=1)
    ttk.Label(dice, text='O').grid(column=1, row=1)
    ttk.Label(dice, text=' ').grid(column=2, row=1)
    ttk.Label(dice, text='O').grid(column=0, row=2)
    ttk.Label(dice, text=' ').grid(column=1, row=2)
    ttk.Label(dice, text='O').grid(column=2, row=2)

def six(*args): 
    removePrev()
    ttk.Label(dice, text='O').grid(column=0, row=0)
    ttk.Label(dice, text=' ').grid(column=1, row=0)
    ttk.Label(dice, text='O').grid(column=2, row=0)
    ttk.Label(dice, text='O').grid(column=0, row=1)
    ttk.Label(dice, text=' ').grid(column=1, row=1)
    ttk.Label(dice, text='O').grid(column=2, row=1)
    ttk.Label(dice, text='O').grid(column=0, row=2)
    ttk.Label(dice, text=' ').grid(column=1, row=2)
    ttk.Label(dice, text='O').grid(column=2, row=2)
#==============================================FUNCTIONS===================================================================

diceComponents = [one, two, three, four, five, six]                         # put all my dice functions in 1 list

roll = ttk.Button(root, text='Roll', command=diceComponents[randint(0, 5)])

dice.grid(column=0, row=0)
roll.grid(column=0, row=1)

default()


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()

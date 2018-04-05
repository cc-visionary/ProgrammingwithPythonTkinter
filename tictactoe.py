"""
This is the TicTacToe game I built which you basically play tictactoe in.

@bugs:
    - if you click the other clickable buttons even if a player already won, the result will be set to a draw if there are no clickable buttons left.(unfixed)
    - if you have the last turn and you win at the very very last turn, it will result into a draw instead of a win for you.(unfixed)

@author: Christopher 04/03/2018 2:05PM
"""

from tkinter import *
from tkinter import ttk

#=================================================Functions==============================================

def click(button):
    global nextClick

    if nextClick == 'X':
        button['text'] = 'X'
        nextClick = 'O'

    else:
        button['text'] = 'O'
        nextClick = 'X'

    button.state(['disabled'])

def point(*args):
    # checks top-left button
    if tl['text'] == 'X':
        if (tl['text'] == tc['text'] and tc['text'] == tr['text']) or (tl['text'] == cl['text'] and cl['text'] == bl['text']):
            win('Player 1')
        else:
            pass
    elif tl['text'] == 'O':
        if (tl['text'] == tc['text'] and tc['text'] == tr['text']) or (tl['text'] == cl['text'] and cl['text'] == bl['text']):
            win('Player 2')
        else:
            pass
    else:
        pass

    # checks center-center button
    if cc['text'] == 'X':
        if (tl['text'] == cc['text'] and cc['text'] == br['text']) or (bl['text'] == cc['text'] and cc['text'] == tr['text']) or (cl['text'] == cc['text'] and cc['text'] == cr['text']) or (tc['text'] == cc['text'] and cc['text'] == bc['text']):
            win('Player 1')
        else:
            pass
    elif cc['text'] == 'O':
        if (tl['text'] == cc['text'] and cc['text'] == br['text']) or (bl['text'] == cc['text'] and cc['text'] == tr['text']) or (cl['text'] == cc['text'] and cc['text'] == cr['text']) or (tc['text'] == cc['text'] and cc['text'] == bc['text']):
            win('Player 2')
        else:
            pass
    else:
        pass

    # checks bottom-right button
    if br['text'] == 'X':
        if (bl['text'] == bc['text'] and bc['text'] == br['text']) or (tr['text'] == cr['text'] and cr['text'] == br['text']):
            win('Player 1')
        else:
            pass
    elif br['text'] == 'O':
        if (bl['text'] == bc['text'] and bc['text'] == br['text']) or (tr['text'] == cr['text'] and cr['text'] == br['text']):
            win('Player 2')
        else:
            pass
    else:
        pass

    if tl.instate(['disabled']) and tc.instate(['disabled']) and tr.instate(['disabled']) and cl.instate(['disabled']) and cc.instate(['disabled']) and cr.instate(['disabled']) and bl.instate(['disabled']) and bc.instate(['disabled']) and br.instate(['disabled']):
        draw()
    else:
        pass


def win(player,*args):
    whoWins.set(player + ' wins!')

def draw():
    whoWins.set("It's a draw!")
#=================================================Functions==============================================

root = Tk()
root.title('Tic Tac Toe')
root.geometry('250x200')
ttk.Label(root, text='Tic Tac Toe').grid(column=0, row=0)

#==================================================Game Frame=======================================================

gameFrame = ttk.Frame(root, padding='10 10 10 10')
gameFrame.grid(column=0, row=1)

tl = ttk.Button(gameFrame, command=lambda:[click(tl), point()]) #top-left
tc = ttk.Button(gameFrame, command=lambda:[click(tc), point()]) #top-center
tr = ttk.Button(gameFrame, command=lambda:[click(tr), point()]) #top-right
cl = ttk.Button(gameFrame, command=lambda:[click(cl), point()]) #center-left
cc = ttk.Button(gameFrame, command=lambda:[click(cc), point()]) #center-center
cr = ttk.Button(gameFrame, command=lambda:[click(cr), point()]) #center-right
bl = ttk.Button(gameFrame, command=lambda:[click(bl), point()]) #bottom-left
bc = ttk.Button(gameFrame, command=lambda:[click(bc), point()]) #bottom-center
br = ttk.Button(gameFrame, command=lambda:[click(br), point()]) #bottom-right

nextClick = 'X'
player1 = 0
player2 = 0

tl.grid(row=0, column=0)
tc.grid(row=0, column=1)
tr.grid(row=0, column=2)
cl.grid(row=1, column=0)
cc.grid(row=1, column=1)
cr.grid(row=1, column=2)
bl.grid(row=2, column=0)
bc.grid(row=2, column=1)
br.grid(row=2, column=2)

for buttons in gameFrame.winfo_children(): buttons.configure(width=4)

#==================================================Game Frame=======================================================

whoWins = StringVar()

ttk.Label(root, font=('monospace', 20), textvariable=whoWins).grid(row=2, column=0)

root.mainloop()

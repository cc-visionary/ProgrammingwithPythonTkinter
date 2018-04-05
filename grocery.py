"""
Grocery

This Grocery program is program that I made that has a list box that users can choose unto and
select how many number of item they want of that item in the combo box and adds it to their cart.
And has a lot more other features like remove unwanted items from the cart, checkout, and print receipt.
This program also records the log of each command shown in the console.

@author: Christopher Lim 04/04/2018 4:20PM
"""

from tkinter import *
from tkinter import ttk

#======================================================FUNCTIONS============================================================
def showPrice(*args): # shows the price of the item
    idxs = products.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        price = prices[wholeList[idx]]
        item = wholeList[idx]
        pricemsg.set('%s is %s peso' % (item, price))

def add(*args): # adds the selected item and the number of items to be bought in the cart
    idxs = products.curselection()
    cart.insert(END, str(amountOf.get()) + ' ' + str(wholeList[idxs[0]]))
    print('Added ' + str(amountOf.get()) + ' ' + str(wholeList[idxs[0]]) + ' to cart')


def remove(*args): # removes the selected item in the cart
     idxs = cart.curselection()
     cart.delete(idxs[0])
     print('Removed index ' + str(idxs[0]) + ' from cart' )

def checkOut(*args): # creates a new window in checkout and shows the receipt
    print('Check out')

    count = 2
    totalPrice = 0

    receipt = Tk()
    receipt.title('Receipt')
    receipt.resizable(False, False)
    ttk.Label(receipt, text='Receipt').grid(row=0, column=0, columnspan=3, pady=5)
    ttk.Label(receipt, text='Amount').grid(row=1, column=0, padx=5, pady=5)
    ttk.Label(receipt, text='Item').grid(row=1, column=1, padx=5, pady=5)
    ttk.Label(receipt, text='Price').grid(row=1, column=2, padx=5, pady=5)
    for x in enumerate(cart.get(0, END)):
        items = x[1].split(' ')
        amount = int(items[0])
        item = items[1]
        itemPrice = amount * prices[item]
        totalPrice += itemPrice
        ttk.Label(receipt, text=amount).grid(row=count, column=0, padx=5)
        ttk.Label(receipt, text=item).grid(row=count, column=1, padx=5)
        ttk.Label(receipt, text=itemPrice).grid(row=count, column=2, padx=5)
        count += 1
    ttk.Label(receipt, text='Total').grid(row=count, column=1)
    ttk.Label(receipt, text=totalPrice).grid(row=count, column=2)
    ttk.Button(receipt, text='Print', command=p).grid(row=count+1, column=0, columnspan=3) # print feature
    
def p(*args):
    print('Printing...')
    print('Print Succesful')
#======================================================FUNCTIONS============================================================

root = Tk()
root.title('Grocery')
root.geometry('380x500')
root.resizable(False, False)
# root.minsize(380, 500)
# root.maxsize(1000, 600)

lblFrame = ttk.Label(root, text='Grocery', font=('monospace', 30))

#TODO have a filtering system
vegetableList = ('Carrots', 'Onions', 'Tomatoes', 'Lettuce', 'Cabbage', 'Kale')
fruitList = ('Banana', 'Orange', 'Watermelon', 'Grapes', 'Peaches', 'Apple')
wholeList = vegetableList + fruitList
prices = {'Carrots': 50.00, 'Onions': 30.00, 'Tomatoes': 40.00, 'Lettuce': 30.00, 'Cabbage': 20.00, 'Kale': 100.00,
          'Banana': 30.00, 'Orange': 60.00, 'Watermelon': 130.00, 'Grapes': 110.00, 'Peaches': 80.00, 'Apple': 50.00}
prodList = StringVar(value=wholeList)
pricemsg = StringVar()

print('Log: ') # the log shown in the console

shopFrame = ttk.Frame(root, padding='8 8 12 12') 
lblItems = ttk.Label(shopFrame, text='Available Products:', font=('monospace', 20))
lblPrice = ttk.Label(shopFrame, textvariable=pricemsg)
products = Listbox(shopFrame, listvariable=prodList, height=10, width=30)

buttonFrame = ttk.Frame(shopFrame)
addToCart = ttk.Button(buttonFrame, text='Add to Cart', command=add, width=15)
checkOut = ttk.Button(buttonFrame, text='Check out', command=checkOut, width=15)

# Number of Items to be bought
amountOf = StringVar()

lblAmount = ttk.Label(buttonFrame, text='Amount')
amount = Spinbox(buttonFrame, from_=1, to=100, textvariable=amountOf, width=3)

# Cart Frame
cartList = StringVar()

cartFrame = ttk.Frame(root, padding='8 8 12 12')

cart = Listbox(cartFrame, height=10, width=40, listvariable=cartList)
lblCart = ttk.Label(cartFrame, text='Cart:', font=('monospace', 20))
removeFromCart = ttk.Button(cartFrame, text='Remove from Cart', command=remove)

lblFrame.grid(column=0, row=1, sticky=(N, W))
shopFrame.grid(column=0, row=2, sticky=(N, S, E, W))
lblItems.grid(column=0, row=1, stick=W)
products.grid(column=0, row=2, rowspan=2, sticky=(N, W, E))
lblPrice.grid(column=1, row=3, sticky=(N, W, E), padx=5)

buttonFrame.grid(column=1, row=3, sticky=(W, E, S))
lblAmount.grid(column=0, row=0, sticky=W, padx=5)
amount.grid(column=0, row=1, padx=5, sticky=(W, E))
addToCart.grid(column=0, row=2, sticky=(W, E, S), padx=5)
checkOut.grid(column=0, row=3, sticky=(W, E, S), padx=5)

cartFrame.grid(column=0, row=3, sticky=(N, S, E, W))
lblCart.grid(column=0, row=0, sticky=W)
cart.grid(column=0, row=1, sticky=(N, W, E))
removeFromCart.grid(column=1, row=1, sticky=(S, W), padx=5)

products.bind('<<ListboxSelect>>', showPrice)

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)
# root.rowconfigure(2, weight=1)
# shopFrame.columnconfigure(0, weight=3)
# shopFrame.columnconfigure(1, weight=1)
# shopFrame.rowconfigure(0, weight=1)
# shopFrame.rowconfigure(1, weight=3)
# shopFrame.rowconfigure(2, weight=1)
# shopFrame.rowconfigure(3, weight=1)
# cartFrame.columnconfigure(0, weight=3)
# cartFrame.columnconfigure(1, weight=1)
# cartFrame.rowconfigure(0, weight=1)
# cartFrame.rowconfigure(1, weight=1)
# buttonFrame.columnconfigure(0, weight=1)
# buttonFrame.rowconfigure(0, weight=1)
# buttonFrame.rowconfigure(1, weight=1)

root.mainloop()

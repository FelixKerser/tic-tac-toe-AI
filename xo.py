import random
from tkinter import *
import os
import sys

root = Tk()

root['bg'] = '#D0CFE1'
root.title('tic tac toe')
root.geometry('600x600')
root.resizable(width=True, height=True)

frame1 = Frame(root, bg = '#9765E1')
frame1.place(relx=0.15, rely=0, relwidth=0.7, relheight=0.05)

labeltop = Label(frame1, text='X - you  O - bot')
labeltop.pack(side=TOP)

root.mainloop()
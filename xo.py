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

frame2 = Frame(root, bg = '#C1A8E1')
frame2.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.6)

left_top = False
center_top = False
right_top = False
left_center = False
center_center = False
right_center = False
center_bottom = False
left_bottom = False
right_bottom = False


#top

def move_left_top():
    global left_top
    left_top = True
    button_left_top.place_forget()
    button_left_top_x = Label(frame2, text='X', font=80)
    button_left_top_x.place(relx=0.15, rely=0.2)
    move_ai()

def move_center_top():
    global center_top
    center_top = True

def move_right_top():
    global right_top
    right_top = True



#center


def move_left_center():
    global left_center
    left_center = True

def move_center_center():
    global center_center
    center_center = True

def move_right_center():
    global right_center
    right_center = True



#bottom


def move_left_bottom():
    global left_bottom
    left_bottom = True

def move_center_bottom():
    global center_bottom
    center_bottom = True 

def move_right_bottom():
    global right_top
    right_top = True   



def move_ai():
    if left_top == True:
        if center_center != True:
            button_center_center.place_forget()
            button_center_center_x = Label(frame2, text='O', font=80)
            button_center_center_x.place(relx=0.47, rely=0.5)



#top

button_left_top = Button(frame2, text="X",
 width=3,height=1, command=move_left_top)
button_left_top.place(relx=0.15, rely=0.2)

button_center_top = Button(frame2, text="X",
 width=3,height=1, command=move_center_top)
button_center_top.place(relx=0.47, rely=0.2)

button_right_top = Button(frame2, text="X",
 width=3,height=1, command=move_right_top)
button_right_top.place(relx=0.8, rely=0.2)



#center


button_left_center = Button(frame2, text="X",
 width=3,height=1, command=move_left_center)
button_left_center.place(relx=0.15, rely=0.5)


button_center_center = Button(frame2, text="X",
 width=3,height=1, command=move_center_center)
button_center_center.place(relx=0.47, rely=0.5)


button_right_center = Button(frame2, text="X",
 width=3,height=1, command=move_right_center)
button_right_center.place(relx=0.8, rely=0.5)




#bottom


button_left_bottom = Button(frame2, text="X",
 width=3,height=1, command=move_left_bottom)
button_left_bottom.place(relx=0.15, rely=0.8)


button_center_bottom = Button(frame2, text="X",
 width=3,height=1, command=move_center_bottom)
button_center_bottom.place(relx=0.47, rely=0.8)


button_right_bottom = Button(frame2, text="X",
 width=3,height=1, command=move_right_bottom)
button_right_bottom.place(relx=0.8, rely=0.8)


root.mainloop()
#29.01.2020
#по шаблону доделать ИИ и все варианты ходов

#30.01.2020
#продолжения хода бота, по какой-то причине просто отказывается ходить. Скорее всего проблема в условиях

#07.2.2020
#бот может выиграть просто так, и по каким-то причинам не ходит, сделать тестирования

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

you_win = False
bot_win = False
nobody_win = False

bot_left_top = False
bot_center_top = False
bot_right_top = False
bot_left_center = False
bot_center_center = False
bot_right_center = False
bot_center_bottom = False
bot_left_bottom = False
bot_right_bottom = False

left_top = False
center_top = False
right_top = False
left_center = False
center_center = False
right_center = False
center_bottom = False
left_bottom = False
right_bottom = False

first_tactic = True

def move_ai_first():
    global first_move, bot_left_top, bot_center_top, bot_right_top, bot_left_center, bot_center_center, bot_right_center, bot_center_bottom, bot_left_bottom, bot_right_bottom
    first_move = True
    #move
    if left_top != True:
        bot_left_top = True
        button_left_top.place_forget()
        button_left_top_x = Label(frame2, text='O', font=80)
        button_left_top_x.place(relx=0.15, rely=0.2)
    else:
        if left_bottom != True:
            bot_left_bottom = True
            button_left_bottom.place_forget()
            button_left_bottom_x = Label(frame2, text='O', font=80)
            button_left_bottom_x.place(relx=0.15, rely=0.8)
        else:
            if right_center != True:
                bot_right_center = True
                button_right_center.place_forget()
                button_right_center_x = Label(frame2, text='O', font=80)
                button_right_center_x.place(relx=0.8, rely=0.5)

def move_ai_second():
    global second_move, bot_left_top, bot_center_top, bot_right_top, bot_left_center, bot_center_center, bot_right_center, bot_center_bottom, bot_left_bottom, bot_right_bottom
    second_move = True
    #move
    if left_center and center_center == True:
        if bot_right_center != True:
            bot_right_center = True
            button_right_center.place_forget()
            button_right_center_x = Label(frame2, text='O', font=80)
            button_right_center_x.place(relx=0.8, rely=0.5)
    else:
        if right_center and center_center == True:
            bot_left_center = True
            button_left_center.place_forget()
            button_left_center_x = Label(frame2, text='O', font=80)
            button_left_center_x.place(relx=0.15, rely=0.5)
        else:
            if left_bottom != True:
                bot_left_bottom = True
                button_left_bottom.place_forget()
                button_left_bottom_x = Label(frame2, text='O', font=80)
                button_left_bottom_x.place(relx=0.15, rely=0.8)
            else:
                if center_bottom != True:
                    bot_center_bottom = True
                    button_center_bottom.place_forget()
                    button_center_bottom_x = Label(frame2, text='O', font=80)
                    button_center_bottom_x.place(relx=0.47, rely=0.8)
                else:
                    if right_bottom != True:
                        bot_right_bottom = True
                        button_right_bottom.place_forget()
                        button_right_bottom_x = Label(frame2, text='O', font=80)
                        button_right_bottom_x.place(relx=0.8, rely=0.8)
                    else:
                        if right_top != True:
                            bot_right_top = True
                            bot_right_top = True
                            button_right_top.place_forget()
                            button_right_top_x = Label(frame2, text='O', font=80)
                            button_right_top_x.place(relx=0.8, rely=0.2)


def move_ai_third():
    global third_move, bot_left_top, bot_center_top, bot_right_top, bot_left_center, bot_center_center, bot_right_center, bot_center_bottom, bot_left_bottom, bot_right_bottom
    third_move = True
    #move
    if right_top != True:
        if bot_left_top == True:
            bot_right_top = True
            button_right_top.place_forget()
            button_right_top_x = Label(frame2, text='O', font=80)
            button_right_top_x.place(relx=0.8, rely=0.2)
    else:
        if left_bottom != True:
            if bot_left_top or bot_left_center == True:    
                bot_left_bottom = True
                button_left_bottom.place_forget()
                button_left_bottom_x = Label(frame2, text='O', font=80)
                button_left_bottom_x.place(relx=0.15, rely=0.8)
        else:
            if center_bottom != True:
                if bot_left_bottom or bot_right_bottom == True:    
                    bot_center_bottom = True
                    button_center_bottom.place_forget()
                    button_center_bottom_x = Label(frame2, text='O', font=80)
                    button_center_bottom_x.place(relx=0.47, rely=0.8)
            else:
                if bot_left_bottom or bot_center_bottom == True:
                    if right_bottom != True:
                        bot_right_bottom = True
                        button_right_bottom.place_forget()
                        button_right_bottom_x = Label(frame2, text='O', font=80)
                        button_right_bottom_x.place(relx=0.8, rely=0.8)
                else:
                    if right_top and bot_right_top != True:
                        bot_right_top = True
                        button_right_top.place_forget()
                        button_right_top_x = Label(frame2, text='O', font=80)
                        button_right_top_x.place(relx=0.8, rely=0.2)
                    else:
                        if center_bottom and bot_center_bottom != True:
                            bot_center_bottom = True
                            button_center_bottom.place_forget()
                            button_center_bottom_x = Label(frame2, text='O', font=80)
                            button_center_bottom_x.place(relx=0.47, rely=0.8)
                        else:
                            if left_center and bot_left_center != True:
                                bot_left_center = True
                                button_left_center.place_forget()
                                button_left_center_x = Label(frame2, text='O', font=80)
                                button_left_center_x.place(relx=0.15, rely=0.5)
                            else:
                                if right_bottom and bot_right_bottom != True:
                                    bot_right_bottom = True
                                    button_right_bottom.place_forget()
                                    button_right_bottom_x = Label(frame2, text='O', font=80)
                                    button_right_bottom_x.place(relx=0.8, rely=0.8)

def move_ai_fourth():
    global fourth_move, bot_left_top, bot_center_top, bot_right_top, bot_left_center, bot_center_center, bot_right_center, bot_center_bottom, bot_left_bottom, bot_right_bottom
    fourth_move = True
    if you_win and bot_win != True:
        winletter = Label(frame2, text="Nobody win", font=70)
        winletter.pack(side='bottom')
    #move
    if center_top != True:
        bot_center_top = True
        button_center_top.place_forget()
        button_center_top_x = Label(frame2, text='O', font=80)
        button_center_top_x.place(relx=0.47, rely=0.2)
    else:
        if right_bottom != True:
            bot_right_bottom = True
            button_right_bottom.place_forget()
            button_right_bottom_x = Label(frame2, text='O', font=80)
            button_right_bottom_x.place(relx=0.8, rely=0.8)
        else:
            if right_center and bot_right_center != True:
                bot_right_center = True
                button_right_center.place_forget()
                button_right_center_x = Label(frame2, text='O', font=80)
                button_right_center_x.place(relx=0.8, rely=0.5)

def move_ai_fifth():
    global fifth_move, bot_left_top, bot_center_top, bot_right_top, bot_left_center, bot_center_center, bot_right_center, bot_center_bottom, bot_left_bottom, bot_right_bottom
    fifth_move = True
    if you_win and bot_win != True:
        winletter = Label(frame2, text="Nobody win", font=70)
        winletter.pack(side='bottom')
    #move
    if center_top != True:
        bot_center_top = True
        button_center_top.place_forget()
        button_center_top_x = Label(frame2, text='O', font=80)
        button_center_top_x.place(relx=0.47, rely=0.2)
    
    else:
        if right_center != True:
            bot_right_center = True
            button_right_center.place_forget()
            button_right_center_x = Label(frame2, text='O', font=80)
            button_right_center_x.place(relx=0.8, rely=0.5)
        else:
            if center_bottom != True:
                bot_center_bottom = True
                button_center_bottom.place_forget()
                button_center_bottom_x = Label(frame2, text='O', font=80)
                button_center_bottom_x.place(relx=0.47, rely=0.8)
                


def check_win():
    global you_win, nobody_win, bot_win, center_top, right_top, left_top, left_center, left_bottom, center_center, right_center, center_bottom, right_bottom,\
     bot_center_top, bot_right_top, bot_left_top, bot_left_center, bot_left_bottom, bot_center_center, bot_right_center, bot_center_bottom, bot_right_bottom
    #win player
    if you_win == False:
        if left_top and center_top and right_top == True:
            you_win = True
            winletter = Label(frame2, text="You win!", font=70)
            winletter.pack(side='bottom')
        else:
            if left_top and left_center and left_bottom == True:
                you_win = True
                winletter = Label(frame2, text="You win!", font=70)
                winletter.pack(side='bottom')
            else:
                if left_center and center_center and right_center == True:
                    you_win = True
                    winletter = Label(frame2, text="You win!", font=70)
                    winletter.pack(side='bottom')
                else:
                    if left_bottom and center_bottom and right_bottom == True:
                        you_win = True
                        winletter = Label(frame2, text="You win!", font=70)
                        winletter.pack(side='bottom')
                    else:
                        if right_top and right_center and right_bottom == True:
                            you_win = True
                            winletter = Label(frame2, text="You win!", font=70)
                            winletter.pack(side='bottom')
                        else:
                            if center_top and center_center and center_bottom == True:
                                you_win = True
                                winletter = Label(frame2, text="You win!", font=70)
                                winletter.pack(side='bottom')
                            else:
                                if left_top and center_center and right_bottom == True:
                                    you_win = True
                                    winletter = Label(frame2, text="You win!", font=70)
                                    winletter.pack(side='bottom')
                                else:
                                    if right_top and center_top and left_bottom == True:
                                        you_win = True
                                        winletter = Label(frame2, text="You win!", font=70)
                                        winletter.pack(side='bottom')

    if bot_win == False:
        #win bot
        if bot_left_top and bot_center_top and bot_right_top == True:
            bot_win = True
            winletter = Label(frame2, text="Bot win...", font=70)
            winletter.pack(side='bottom')

        if bot_left_top and bot_left_center and bot_left_bottom == True:
            bot_win = True
            winletter = Label(frame2, text="Bot win...", font=70)
            winletter.pack(side='bottom')

        if bot_left_center and bot_center_center and bot_right_center == True:
            bot_win = True
            winletter = Label(frame2, text="Bot win...", font=70)
            winletter.pack(side='bottom')

        if bot_left_bottom and bot_center_bottom and bot_right_bottom == True:
            bot_win = True
            winletter = Label(frame2, text="Bot win...", font=70)
            winletter.pack(side='bottom')

        if bot_right_top and bot_right_center and bot_right_bottom == True:
            bot_win = True
            winletter = Label(frame2, text="Bot win...", font=70)
            winletter.pack(side='bottom')

        if bot_center_top and bot_center_center and bot_center_bottom == True:
            bot_win = True
            winletter = Label(frame2, text="Bot win...", font=70)
            winletter.pack(side='bottom')

        if bot_left_top and bot_center_center and bot_right_bottom == True:
            bot_win = True
            winletter = Label(frame2, text="Bot win...", font=70)
            winletter.pack(side='bottom')

        if bot_right_top and bot_center_top and bot_left_bottom == True:
            bot_win = True
            winletter = Label(frame2, text="Bot win...", font=70)
            winletter.pack(side='bottom')

first = True
second = True
third = True
fourth = True

def check_move():
    global first_move, second_move, third_move, fourth_move, fifth_move, first, second, third, fourth
    while True:
        if first_move == True:
            first = False
        else:
            move_ai_first()
            break

        if first == False:
            second = False
            if second_move == True:
                pass
            else:
                move_ai_second()
                break

        if second == False:
            third = False
            if third_move == True:
                pass
            else:
                move_ai_third()
                check_win()
                break
        if third == False:
            fourth = False
            if fourth_move == True:
                pass
            else:
                move_ai_fourth()
                check_win()
                break
        if fourth == False:
            fifth = True
            if fifth_move == True:
                pass
            else:
                move_ai_fourth()
                check_win()
                break



#top

def move_left_top():
    global left_top
    left_top = True
    button_left_top.place_forget()
    button_left_top_x = Label(frame2, text='X', font=80)
    button_left_top_x.place(relx=0.15, rely=0.2)
    check_move()

def move_center_top():
    global center_top
    center_top = True
    button_center_top.place_forget()
    button_center_top_x = Label(frame2, text='X', font=80)
    button_center_top_x.place(relx=0.47, rely=0.2)
    check_move()

def move_right_top():
    global right_top
    right_top = True
    button_right_top.place_forget()
    button_right_top_x = Label(frame2, text='X', font=80)
    button_right_top_x.place(relx=0.8, rely=0.2)
    check_move()



#center


def move_left_center():
    global left_center
    left_center = True
    button_left_center.place_forget()
    button_left_center_x = Label(frame2, text='X', font=80)
    button_left_center_x.place(relx=0.15, rely=0.5)
    check_move()

def move_center_center():
    global center_center
    center_center = True
    button_center_center.place_forget()
    button_center_center_x = Label(frame2, text='X', font=80)
    button_center_center_x.place(relx=0.47, rely=0.5)
    check_move()

def move_right_center():
    global right_center
    right_center = True
    button_right_center.place_forget()
    button_right_center_x = Label(frame2, text='X', font=80)
    button_right_center_x.place(relx=0.8, rely=0.5)
    check_move()



#bottom


def move_left_bottom():
    global left_bottom
    left_bottom = True
    button_left_bottom.place_forget()
    button_left_bottom_x = Label(frame2, text='X', font=80)
    button_left_bottom_x.place(relx=0.15, rely=0.8)
    check_move()

def move_center_bottom():
    global center_bottom
    center_bottom = True 
    button_center_bottom.place_forget()
    button_center_bottom_x = Label(frame2, text='X', font=80)
    button_center_bottom_x.place(relx=0.47, rely=0.8)
    check_move()

def move_right_bottom():
    global right_bottom
    right_bottom = True   
    button_right_bottom.place_forget()
    button_right_bottom_x = Label(frame2, text='X', font=80)
    button_right_bottom_x.place(relx=0.8, rely=0.8)
    check_move()

first_move = False
second_move = False
third_move = False
fourth_move = False
fifth_move = False


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
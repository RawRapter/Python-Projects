"""
Match pair is a card game in which all of the cards are laid face down on a surface
and two cards are flipped face up over each turn.

Game Rule:
- If both the Cards matches then it remains flipped.
- If wrong choosen then it will hide again.
- There is No time limit.
- Try your best to memorize.
"""
#Importing required Library
import random
import time
from tkinter import Tk , Button , DISABLED

#Function created for commands to be used by button.
def show_symbol(x: int,y: int):
    global first
    global previousx , previousy
    #Passing symbols to the button.
    buttons[x,y]['text'] = button_symbols[x,y]
    #updates_idletasks updates the idle pending task that is stable or not updating in the application for some reason. 
    #It calls all the events that are pending without processing any other events or callback.
    buttons[x,y].update_idletasks()

    if first:
        previousx = x
        previousy = y
        #Making first false when it first card is clicked.
        first = False
    #Second card click
    elif previousx != x or previousy != y:
        #if second card doesnt matches first card.
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            #flipping card
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        #if first and second card matches then command disables for them.
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        #making first true again for next turn
        first = True
#Creating window
win = Tk()
win.title('Match Pair') #Title Provided
win.resizable(width=False , height=False) #Ristricting Window resize option

#First Card choosen variable
first = True

#Variables to remember which card are choosen by storing there coordinates
previousx = 0
previousy = 0

#Creating empty dictionary for buttons and button symbol.
buttons = { }
button_symbols = { }

#All symbols list
symbols = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
            u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

#shuffling the symbols
random.shuffle(symbols)

#Loops to create 24 buttons in the form of card.
for x in range(6):
    for y in range(4):
        #using lambda in command such that coordinates changes at every iteration.
        #If lambda is not used then coordinate error will come as every time (0,0) will get pass.
        button = Button(command = lambda x=x , y=y: show_symbol(x,y) , width = 10, height = 8)
        button.grid(column = x , row = y)
        #Adding buttons and symbols into the dictionary to be used in command
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()

#Ending the Window
win.mainloop()
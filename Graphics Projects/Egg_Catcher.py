"""
This Project is a game , name - Egg Catcher.
"""

#Importing libraries
from itertools import cycle
from random import randrange
from tkinter import Tk , Canvas , messagebox , font

#Creating variable for canvas size
canvas_width = 800
canvas_height = 400

win = Tk() #Win starts
#Giving title
win.title("The Egg Catcher")
#creating canvas
c = Canvas(win , width = canvas_width ,  height = canvas_height , background = 'deep sky blue')
#creating ground
c.create_rectangle(-5, canvas_height - 100 , canvas_width + 5 , canvas_height + 5 , fill='sea green', width=0)
#creating sun
c.create_oval(-80,-80,120,120,fill='orange' , width=0)
c.pack() #canvas packed

#creating list of colors which which will be repeated
color_cycle = cycle(['light blue' , 'light pink' , 'light yellow','light green' , 'red', 'blue' , 'green','black'])

#Creating variables for egg size,shape and movement
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

#Creating variables for basket to catch eggs
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height -catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

#Creating catcher (Arc)
catcher = c.create_arc(catcher_start_x ,catcher_start_y ,catcher_start_x2,catcher_start_y2 , start=200 , extent = 140 , style='arc' , outline=catcher_color , width=3)

#Intializing score and creating it's Text
score = 0
score_text = c.create_text(10,10,anchor='nw' , font=('Arial',18,'bold'),fill='darkblue',text='Score : ' + str(score))

#Initializing Life and creating it's Text
lives_remaning = 3
lives_text = c.create_text(canvas_width-10,10,anchor='ne' , font=('Arial',18,'bold'),fill='darkblue',text='Lives Left: ' + str(lives_remaning))

#Creating empty
eggs = []

""" Defining functions for game play"""

#Creating Egg, setting their height and range of falling
def create_eggs():
    x = randrange(10,740) #to drop from random position
    y = 40 #fixing height from height where it will fall
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0) #creating eggss
    eggs.append(new_egg) #adding the egg to the list
    win.after(egg_interval,create_eggs) #recursive after given interval

#Defining egg movement(i.e changing their positions)
def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg) #getting coordinates
        c.move(egg,0,10) #dropping by 10
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    win.after(egg_speed,move_eggs)

#Removing the egg from list to over the fame
def egg_dropped(egg):
    eggs.remove(egg) #removing egg
    c.delete(egg) 
    lose_a_life() #functon to decrease life
    if lives_remaning == 0: #when lvies become 0
        messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score))
        win.destroy() #exiting window

#Decreasing a life score by 1
def lose_a_life():
    global lives_remaning
    lives_remaning -= 1
    #configuring the lives text.
    c.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))

#Function to check if catcher catches eggs
def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher) #getting coordinates of catcher
    for egg in eggs: #running loop through egg list
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg) #getting coordinates of egg
        if catcher_x < egg_x and egg_x2  < catcher_x2 and catcher_y2 - egg_y2 < 40: #fixing location such that eggs fall under catcher
            eggs.remove(egg) #removing egg from list
            c.delete(egg) #deleting egg
            increase_score(egg_score) #increasing score
    win.after(100,catch_check) #repeating check

#Function for increasing the score
def increase_score(points):
    global score , egg_speed , egg_interval #creating global variables
    score += points #scores increase every time by 10
    egg_speed = int(egg_speed * difficulty_factor) #increasing speed
    egg_interval = int(egg_interval * difficulty_factor) #decreasing interval
    c.itemconfigure(score_text , text='Score : ' + str(score)) #changing score text

#to make catcher move left
def move_left(event):
    (x1,y1,x2,y2) = c.coords(catcher) #getting coordinates
    if x1 > 0: #boundary check
        c.move(catcher,-20,0) #shifting left

#to make catcher move right
def move_right(event):
    (x1,y1,x2,y2) = c.coords(catcher) #getting coordinates
    if x2 < canvas_width: #boundary check
        c.move(catcher,20,0) #shifting right

#binding keys with function
c.bind('<Left>' , move_left)
c.bind('<Right>' , move_right)
c.focus_set()

#starting the game function to start dropping eggs
win.after(1000,create_eggs)
win.after(1000,move_eggs)
win.after(1000,catch_check)

win.mainloop() #Win ends
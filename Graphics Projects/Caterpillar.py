"""
This project is a imitation of old snake game that we used to play on mobile.
"""

import turtle as t
import random as rd

#making background color yellow
t.bgcolor('yellow')

#Creating base of Caterpillar turtle which will move across pane
caterpillar = t.Turtle()
caterpillar.shape('square') #making it's shape square
caterpillar.speed(0) 
caterpillar.penup()
caterpillar.hideturtle()

#Creating Leaf turtle for desinging leaf
leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape) #Registring new shape
leaf.shape('leaf') #giving our structure to the leaf
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

#Creating Game Start frame
game_started = False #Game will not start automatically
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',font=('Arial',16,'bold')) #Designing Text
text_turtle.hideturtle()

#Creating Score turle to calculate score
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

#Controlling the Pane limit if caterpillar crosses that then game over
def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpillar.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

#Function when aterpillar crosses area
def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

#Function to display score after ever leaf eaten by caterpillar
def display_score(current_score: int):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y) #setting position at given coordinates
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

#Defining function to place a leaf randomly within the frame
def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def start_game():
    global game_started
    #This condition such that if someone click space during game then it doesnt restarts
    if game_started:
        return
    game_started = True

    #Score Intitalized
    score = 0
    #Starting text cleared
    text_turtle.clear()

    #Intializing Caterpillar size and speed
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    #displaying intial score
    display_score(score)
    #Placing leaf
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        #Comparing distance between caterpillar and leaf turtle
        if caterpillar.distance(leaf)<20:
            place_leaf()
            #Increasing caterpillar length
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1,caterpillar_length,1)
            #Increasing caterpillar speed
            caterpillar_speed = caterpillar_speed + 1
            #Score updated by 10 everytime
            score = score + 10
            display_score(score)
        #When window frame is crossed
        if outside_window():
            game_over()
            break

#Defining arrow key movements
def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

#Movement from keys
t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')

t.listen()
#mainloop tells the window to wait for the user to do something
t.mainloop()
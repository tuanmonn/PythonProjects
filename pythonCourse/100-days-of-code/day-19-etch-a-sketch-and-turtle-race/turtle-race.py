# Practice file

from turtle import Turtle, Screen
import random

is_race_on = False
all_turtles = []
screen = Screen()

# setup the screen size
screen.setup(width=500, height=400)

# create a popup for user input
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red","orange","yellow","green","blue","purple"]

x_base = -230
y_base = -100

def create_turtle(color):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x= x_base,y=y_base)
    all_turtles.append(new_turtle)

for i in colors:
    create_turtle(i)
    y_base += 50

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
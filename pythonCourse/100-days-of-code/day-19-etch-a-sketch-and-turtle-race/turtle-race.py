# Practice file

from turtle import Turtle, Screen


screen = Screen()

# setup the screen size
screen.setup(width=500, height=400)

# create a popup for user input
# user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red","orange","yellow","green","blue","purple"]

x_base = -230
y_base = -100

def create_turtle(color):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(x= x_base,y=y_base)

for i in colors:
    create_turtle(i)
    y_base += 50






screen.exitonclick()
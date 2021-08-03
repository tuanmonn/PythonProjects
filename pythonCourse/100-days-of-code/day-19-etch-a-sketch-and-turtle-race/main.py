# Practice file

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



def move_forward():
    tim.forward(10)

screen.onkey(key= "space", fun=move_forward)
screen.listen()
screen.exitonclick()
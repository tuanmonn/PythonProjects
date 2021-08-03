# Practice file

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



def move_forward():
    tim.forward(10)

def move_upward():
    tim.left(10)

def move_downward():
    tim.right(10)

def move_backward():
    tim.backward(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(key= "d", fun=move_forward)
screen.onkey(key= "w", fun=move_upward)
screen.onkey(key= "a", fun=move_backward)
screen.onkey(key= "s", fun=move_downward)
screen.onkey(key= "c", fun=clear_screen)

screen.listen()
screen.exitonclick()
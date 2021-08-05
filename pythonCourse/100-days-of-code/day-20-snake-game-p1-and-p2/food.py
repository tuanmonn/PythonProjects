from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()              # we do this so don't have to call Turtle again
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
        # set a random coordinate for the food
    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x,rand_y)


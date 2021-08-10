from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.dot(20, "white") --> Don't understand why self.dot doesn't work?
        # self.goto(0, 0)
        # self.hideturtle()

        self.base_heading = 30
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(self.base_heading)

    def move(self):
        self.forward(15)

        # Class solution:
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        # self.goto(new_x, new_y)

    def bounce(self):
        self.setheading(180-self.base_heading)

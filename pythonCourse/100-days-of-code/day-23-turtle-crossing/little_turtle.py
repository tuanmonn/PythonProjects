from turtle import Turtle

STARTING_POSITION = (0,-280)

class LittleTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def level_up(self):
        self.reset_position()


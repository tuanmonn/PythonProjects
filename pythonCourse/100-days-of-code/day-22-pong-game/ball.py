from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_x = 10
        self.move_y = 10

    def move(self):

        self.new_x = self.xcor() + self.move_x
        self.new_y = self.ycor() + self.move_y
        self.goto(self.new_x, self.new_y)

    def bounce_wall(self):
        self.move_y *= -1


# -- my solution
# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         # self.dot(20, "white") --> Don't understand why self.dot doesn't work?
#         # self.goto(0, 0)
#         # self.hideturtle()
#         self.setheading(60)
#
#
#     def move(self):
#         self.forward(15)
#
#     def bounce_wall(self):
#         # My solution 1
#         # self.setheading(self.heading()+120) --> This give weirds bouncing
#
#         # My solution 2
#         if self.ycor() < 0:
#             self.left(60)
#         if self.ycor() > 0:
#             self.right(60)
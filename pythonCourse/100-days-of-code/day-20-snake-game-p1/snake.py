from turtle import Turtle

# My solution
# class Snake:
#     square_list = []
#     def __init__(self):
#         # create snake body
#         base_coor = 0
#         for _ in range(3):
#             new_shape = Turtle("square")        # Can create the shape here
#             new_shape.penup()                   # Turtle doesn't draw
#             new_shape.setx(x=base_coor)         # can use goto()
#             new_shape.color("white")
#             Snake.square_list.append(new_shape)
#             base_coor -= 10
#
#     def move(self):
#         for sq_num in range(len(Snake.square_list) - 1, 0, -1):  # start/stop/step
#             new_pos = Snake.square_list[sq_num - 1].position()
#             Snake.square_list[sq_num].goto(new_pos)
#         Snake.square_list[0].forward(20)


# solution
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        # create snake body
        self.square_list = []
        self.create_snake()
        self.head = self.square_list[0]

    def create_snake(self):
        base_coor = 0
        for _ in range(3):
            new_shape = Turtle("square")        # Can create the shape here
            new_shape.penup()                   # Turtle doesn't draw
            new_shape.setx(x=base_coor)         # can use goto()
            new_shape.color("white")
            self.square_list.append(new_shape)
            base_coor -= 10

    def move(self):
        for sq_num in range(len(self.square_list) - 1, 0, -1):  # start/stop/step
            new_pos = self.square_list[sq_num - 1].position()
            self.square_list[sq_num].goto(new_pos)
        self.square_list[0].forward(MOVE_DISTANCE)              # Set a constant for distance

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
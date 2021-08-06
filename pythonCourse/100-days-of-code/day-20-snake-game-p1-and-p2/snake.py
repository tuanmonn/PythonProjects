from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

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
class Snake(Turtle):

    def __init__(self):
        super().__init__()
        # create snake body
        self.square_list = []
        self.create_snake()
        self.head = self.square_list[0]
        self.speed_base = 1

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)

    def move(self):
        for sq_num in range(len(self.square_list) - 1, 0, -1):  # start/stop/step
            new_pos = self.square_list[sq_num - 1].position()
            self.square_list[sq_num].goto(new_pos)
        self.square_list[0].forward(MOVE_DISTANCE)              # Set a constant for distance

    def extend(self):
        self.add_square(self.square_list[-1].position())

    def add_square(self,position):
        new_shape = Turtle("square")  # Can create the shape here
        new_shape.penup()  # Turtle doesn't draw
        new_shape.goto(position)  # can use goto()
        new_shape.color("white")
        self.square_list.append(new_shape)

    def speed_up(self):
        if self.speed_base < 10:
            self.speed_base += 1
        else:
            self.speed_base = 0
        self.head.speed(self.speed_base)


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
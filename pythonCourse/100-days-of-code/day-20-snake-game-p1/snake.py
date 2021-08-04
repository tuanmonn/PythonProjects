from turtle import Turtle

class Snake():
    square_list = []
    def __init__(self):
        # create snake body
        base_coor = 0
        for _ in range(3):
            new_shape = Turtle("square")        # Can create the shape here
            new_shape.penup()                   # Turtle doesn't draw
            new_shape.setx(x=base_coor)         # can use goto()
            new_shape.color("white")
            Snake.square_list.append(new_shape)
            base_coor -= 10

    def move(self):
        for sq_num in range(len(Snake.square_list) - 1, 0, -1):  # start/stop/step
            new_pos = Snake.square_list[sq_num - 1].position()
            Snake.square_list[sq_num].goto(new_pos)
        Snake.square_list[0].forward(20)
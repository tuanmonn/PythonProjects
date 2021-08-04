from turtle import Turtle, Screen
import random
import time

# Create the screen and its configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)                            # Turn off the screen animation

square_list = []

# Create the snake body
base_coor= 0
for _ in range(3):
    new_shape = Turtle("square")            # Can create the shape here
    new_shape.penup()                       # Turtle doesn't draw
    new_shape.setx(x=base_coor)             # can use goto()
    new_shape.color("white")
    square_list.append(new_shape)
    base_coor -= 10


# Make the snake move
game_is_on = True
while game_is_on:
    screen.update()                                     # only update the screen when all the squares have run
    time.sleep(0.1)                                     # have a delay between each "move"
    for sq_num in range(len(square_list) - 1,0,-1):                         # start/stop/step
        new_pos = square_list[sq_num - 1].position()
        square_list[sq_num].goto(new_pos)
    square_list[0].forward(20)




# Brainstorm: how to make the snake move
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for i in range(0,3):
#         if i == 0:
#             square_list[i].forward(20)
#         if i != 0:
#             square_pos = square_list[i-1].position()
#             square_list[i].setpos(square_pos)












screen.exitonclick()


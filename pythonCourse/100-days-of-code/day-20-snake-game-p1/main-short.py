from turtle import Turtle, Screen
import time
from snake import Snake

# Create the screen and its configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

square_list = []

# Create the snake
create_snake = Snake()

# Make the snake move
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    create_snake.move()












screen.exitonclick()


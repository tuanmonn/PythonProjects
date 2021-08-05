from turtle import Turtle, Screen
import time
from snake import Snake

# Create the screen and its configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# Create the snake
snake = Snake()
screen.listen()                         # start to listen to keystrokes
screen.onkey(snake.up, "Up")            # listen to the event
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Make the snake move
game_is_on = True
while game_is_on:
    screen.update()                     # Refresh the screen
    time.sleep(0.1)
    snake.move()

screen.exitonclick()


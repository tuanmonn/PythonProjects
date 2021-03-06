from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Create the screen and its configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

# Create the snake & food
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


# Make the snake move
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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        snake.speed_up()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if head collides with any segment in the tail -> game over
    for square in snake.square_list[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball
import time


# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)


# Create paddle
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()

# # Make the paddle move
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.distance(right_paddle) < 30 or ball.distance(left_paddle) < 30:
        ball.bounce()

    if ball.ycor() > 200:
        ball.bounce()






screen.exitonclick()
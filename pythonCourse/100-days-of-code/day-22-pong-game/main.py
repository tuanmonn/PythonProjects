from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
paddle_hit = 0


# Create paddle
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()

# Make the paddle move
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# Make the separator
sep_line = Turtle()
sep_line.penup()
sep_line.pencolor("white")
sep_line.hideturtle()
sep_line.goto(0,-300)
sep_line.pensize(5)
sep_line.setheading(90)
for _ in range(30):
    sep_line.pendown()
    sep_line.forward(10)
    sep_line.penup()
    sep_line.forward(10)

# Make score board
scoreboard = ScoreBoard()

# Make the game run
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)             # To make the ball move faster each time it bounces the paddle
    screen.update()
    ball.move()

    # make sure even if the ball hits the side of the paddle it still works
    # set paddle_hit = 0 so it won't continuously bounce
    if paddle_hit == 0:
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_paddle()
            paddle_hit = 1

    else:
        if -320 < ball.xcor() < 320:
            paddle_hit = 0

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.xcor() > 400:
        ball.reset_game()
        scoreboard.update_left_score()

    if ball.xcor() < -400:
        ball.reset_game()
        scoreboard.update_right_score()

    if scoreboard.right_score == 5:
        scoreboard.game_end("Right Paddle")
    elif scoreboard.left_score == 5:
        scoreboard.game_end("Left Paddle")

screen.exitonclick()
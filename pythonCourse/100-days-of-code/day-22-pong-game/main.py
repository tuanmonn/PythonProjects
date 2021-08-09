from turtle import Turtle, Screen
from Paddle import Paddle


# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)


# Create paddle
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))


# # Make the paddle move
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()









screen.exitonclick()
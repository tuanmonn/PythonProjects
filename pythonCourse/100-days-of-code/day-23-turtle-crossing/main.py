from turtle import Turtle, Screen
import time
from little_turtle import LittleTurtle
from car import Car
from level_counter import LevelCounter

# variables
SLEEP_TIME = 0.2

# create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing Project")
screen.tracer(0)

# create a turtle

my_turtle = LittleTurtle()
new_car = Car()
level = LevelCounter()

# make the turtle move
screen.listen()
screen.onkey(my_turtle.move_forward,"Up")
screen.onkey(my_turtle.move_backward,"Down")

# main game
game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    new_car.create_car()
    new_car.car_move()

    if my_turtle.ycor() == 290:
        my_turtle.level_up()
        level.level_up()
        SLEEP_TIME *= 0.6

    for i in new_car.car_list:
        if my_turtle.distance(i) < 20 and my_turtle.ycor() < i.ycor():
            level.game_over()
            game_is_on = False


screen.exitonclick()
from turtle import Turtle
import random
import time

COLORS = ["black","blue","yellow","red","green","orange","pink"]
STARTING_Y_COR = (-250,250)


class Car:
    def __init__(self):
        self.car_list = []                  # create a list to store all the cars

    def create_car(self):
        random_chance = random.randint(1,3)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=-400, y=random.randint(-230,230))
            self.car_list.append(new_car)

    def car_move(self):                     # make all the cars move forward
        for car in self.car_list:
            car.forward(20)

    def speed_up(self):
        self.move_speed *= 0.5
import turtle as turtle
import random

tim = turtle.Turtle()
tim.shape("arrow")
tim.color("blue")

# Make the turtle move
# timmy_turtle.forward(100)
# timmy_turtle.right(90)

# ---- Draw a square
# n = 0
# while n <4:
#     timmy_turtle.forward(100)
#     timmy_turtle.left(90)
#     n += 1

# Another solution
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#

##---- Draw a dash line
# for _ in range(25):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(4)

##---- Draw a triangle, square, penta...
# n = 3
# while n <10:
#     color = "#" + "%06x" % random.randint(0, 0xFFFFFF)
#     tim.pencolor(color)
#     for _ in range(n):
#         angle = float(360/n)
#         tim.forward(100)
#         tim.right(angle)
#     n += 1

# Another solution
# First define a function to draw
# def draw_shape(num_side):
#     angle = 360/num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)
#
# # Then create a for loop to pass in the parameter we want
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)


##---- Draw a random walk
# Line thickness
# tim.pensize(10)
#
# # Angle
# angle = [0, 90, 180, 270]
#
# # speed
# tim.speed(9)
#
# # final
# for _ in range(200):
#     color = "#" + "%06x" % random.randint(0, 0xFFFFFF)
#     tim.pencolor(color)
#     tim.forward(20)
#     tim.right(random.choice(angle))
# another solution for the angle
# tim.setheading(random.choice(direction)) -> This will change the direction, not let the whole pointer spin

##---- Change color mode, generate random rgb color
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0, 255)
#     color_tup = (r,g,b)
#     return color_tup
#
# # Line thickness
# tim.pensize(10)
#
# # Angle
# angle = [0, 90, 180, 270]
#
# # speed
# tim.speed(9)
#
# # final
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(20)
#     tim.right(random.choice(angle))
#

##-----Draw a spirograph
turtle.colormode(255)
tim.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    color_tup = (r,g,b)
    return color_tup

# for _ in range(100):
#     tim.pencolor(random_color())
#     tim.circle(100)
#     tim.left(10)

# solution
def draw_spiro(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spiro(5)


# Need to keep this so the window doesn't disappear
screen = turtle.Screen()
screen.exitonclick()
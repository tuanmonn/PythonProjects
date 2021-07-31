# This version is shorter and easier to understand than the class's solution

import turtle as t
import random
import colorgram

# set the colormode so we can use the rgb
t.colormode(255)

# ---- Run the following code to extract color from the image
# # extract all colors from the photo
# colors = colorgram.extract("wallpaper.jpg",10)
# colors_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tup = (r,g,b)
#     colors_list.append(color_tup)

colors_list = [(2, 31, 84), (10, 113, 148), (244, 144, 100), (247, 60, 101), (11, 56, 131), (248, 106, 133), (24, 174, 155), (2, 89, 106), (197, 7, 104), (248, 208, 190)]

# Main part

tim = t.Turtle()
tim.shape("turtle")
tim.speed(0)

x = -200
y = -200

tim.penup()
tim.setpos(-200,-200) # set the position of the cursor

def draw_row():
    for _ in range(10):
        tim.dot(20,random.choice(colors_list))
        tim.forward(50)

for _ in range(10):
    tim.setpos(x, y)
    draw_row()
    y += 50

tim.hideturtle()

# Need to keep this so the window doesn't disappear
screen = t.Screen()
screen.exitonclick()


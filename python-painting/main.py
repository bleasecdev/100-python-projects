import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract("image.jpg", 30)
# rgb_codes = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_codes.append((r,g,b))

# print(rgb_codes)

colors_list = [(250, 246, 243), (248, 245, 246), (212, 154, 97), 
 (239, 246, 243), (52, 108, 132), (178, 78, 33), (198, 143, 34), 
 (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), 
 (228, 197, 129), (194, 85, 105), (54, 38, 20), 
 (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), 
 (167, 21, 31), (225, 94, 78), (4, 30, 28), 
 (39, 32, 34), (243, 163, 159), (81, 148, 168), 
 (164, 27, 22), (239, 163, 167), 
 (104, 123, 159), (164, 209, 193), 
 (21, 81, 93), (29, 85, 81)]


tim = Turtle()
the_color = random.choice(colors_list)

def change_color(rgb):
    r = rgb[0]
    b = rgb[1]
    g = rgb[2]
    return tim.color(r,b,g)


def paint(dots):
    for _ in range(dots):
        change_color(list(the_color))
        tim.dot()
        tim.penup()
        tim.forward(20)

def canvas(num_of_rows, num_of_dots):
    jump = 0       
    for _ in range(num_of_rows):
        paint(num_of_dots)
        jump-=10
        tim.goto(0,jump)

tim.shape("turtle")
tim.speed("fastest")
canvas(10,10)

screen = Screen()
screen.exitonclick()
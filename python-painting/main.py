import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract("image.jpg", 10)
# rgb_codes = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_codes.append((r,g,b))

# print(rgb_codes)

tim = Turtle()

colors_list = [(250, 246, 243), (248, 245, 246), (212, 154, 97),
(239, 246, 243), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), 
(235, 240, 244), (116, 155, 171)]




def paint(dots):
    for _ in range(dots):
        the_color = random.choice(colors_list)
        tim.pencolor(the_color)
        tim.dot(20)
        tim.penup()
        tim.forward(20)

def draw(num_of_rows, num_of_dots):
    jump = 0       
    for _ in range(num_of_rows):
        paint(num_of_dots)
        jump-=10
        tim.goto(0,jump)


draw(10,10)

screen = Screen()
screen.exitonclick()
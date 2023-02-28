from turtle import Turtle, Screen
import turtle
import random
tim = Turtle()
tim.colormode(255)
tim.shape("turtle")
tim.speed("fastest")


colors_list = [(250, 246, 243), (248, 245, 246), (212, 154, 97),
(239, 246, 243), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), 
(235, 240, 244), (116, 155, 171)]

# def change_color():
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     return tim.color(R,G,B)

def paint(dots):
    for _ in range(dots):
        the_color = random.choice(colors_list)
        R = the_color[0]
        G = the_color[1]
        B = the_color[2]
        tim.pencolor(R, G, B)
        tim.dot()
        tim.penup()
        tim.forward(20)

def canvas(num_of_rows, num_of_dots):
    jump = 0       
    for _ in range(num_of_rows):
        paint(num_of_dots)
        jump-=10
        tim.goto(0,jump)


canvas(20,20)

screen = Screen()
# screen.exitonclick()

# the_color = random.choice(colors_list)
# R = the_color[0]
# G = the_color[1]
# B = the_color[2]
# print(the_color)
# print(R,G,B)
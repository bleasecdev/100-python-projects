from turtle import Turtle, Screen
import random

tim = Turtle()

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    return tim.color(R,G,B)

def paint(dots):
    for _ in range(dots):
        change_color()
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
canvas(20,20)

screen = Screen()
screen.exitonclick()
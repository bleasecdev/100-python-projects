from turtle import Turtle, Screen
import random 

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.pencolor("red")



# def dashed_line():
#     timmy_the_turtle.fd(20)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.fd(20)
#     timmy_the_turtle.pendown()
    


# dashed_line()
# timmy_the_turtle.rt(90)
# dashed_line()
# timmy_the_turtle.rt(90)
# dashed_line()
# timmy_the_turtle.rt(90)
# dashed_line()
# timmy_the_turtle.rt(90)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    return timmy_the_turtle.color(R,G,B)

def triangle():  
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(120)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(120)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(120)



def square():
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(90)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(90)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(90)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(90)



def pentagon(): 
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(72)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(72)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(72)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(72)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(72)



def hexagon():
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(60)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(60)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(60)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(60)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(60)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(60)



def heptagon():
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(51)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(51)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(51)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(51)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(51)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(51)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(51)



def octagon():
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(45)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(45)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(45)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(45)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(45)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(45)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(45)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(45)



def nonagon():
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(40)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(40)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(40)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(40)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(40)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(40)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(40)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(40)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(40)


def decagon():
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)
    timmy_the_turtle.fd(100)
    timmy_the_turtle.rt(36)



# triangle()
# change_color()
# square()
# change_color()
# pentagon()
# change_color()
# hexagon()
# change_color()
# heptagon()
# change_color()
# octagon()
# change_color()
# nonagon()

# Random Walk
# distance = random.randint(5,20)
# directions = [0, 90, 180, 270]

# timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

# for _ in range(200):
#     change_color()
#     timmy_the_turtle.fd(30)
#     timmy_the_turtle.setheading(random.choice(directions))

def draw_spirograph(size):
    for _ in range(int(360 / size)):
        change_color()
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+size)

timmy_the_turtle.dot()

screen = Screen()
screen.exitonclick()  
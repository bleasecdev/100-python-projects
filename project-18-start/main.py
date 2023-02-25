from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.pencolor("red")



def dashed_line():
    timmy_the_turtle.fd(20)
    timmy_the_turtle.penup()
    timmy_the_turtle.fd(20)
    timmy_the_turtle.pendown()
    timmy_the_turtle.fd(20)


dashed_line()
timmy_the_turtle.rt(90)
dashed_line()
timmy_the_turtle.rt(90)
dashed_line()
timmy_the_turtle.rt(90)
dashed_line()
timmy_the_turtle.rt(90)
    


screen = Screen()
screen.exitonclick()
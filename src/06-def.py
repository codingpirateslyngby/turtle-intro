from turtle import Turtle, Screen
from random import random

turtle = Turtle()
turtle.color("yellow")  # color of the line
turtle.getscreen().bgcolor("black")  # background color
turtle.speed(0)

def leaf(pen, size):
    pen.begin_fill()
    pen.fillcolor("green")
    pen.circle(size, 90)
    pen.left(90)
    pen.circle(size, 90)
    pen.end_fill()

size = 200
for n in range(6):
    size = size - 30
    for i in range(12):
        leaf(turtle, size)
        turtle.left(60)

turtle.getscreen().exitonclick()

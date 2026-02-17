from turtle import Turtle, Screen
from random import random

screen = Screen()
screen.bgcolor("black")

turtle = Turtle()
turtle.color("yellow") #color of the line

for i in range(24):
    turtle.forward(random()*100+15)
    turtle.left(60)

screen.exitonclick()

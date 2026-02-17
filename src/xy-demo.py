from turtle import Turtle, Screen
from random import random


t = Turtle()
t.shape("turtle")
t.speed(0)

step = 16
r = 256
g = 0
b = 0
dr = -step
dg = step
db = 0


def colorshift():
    global r, g, b, dr, dg, db
    r = r+dr
    g = g+dg
    b = b+db
    if (r > 255):
        r = 255
        g = 0
        b = 0
        dr = -step
        dg = step
        db = 0
    if (g > 255):
        r = 0
        g = 255
        b = 0
        dr = 0
        dg = -step
        db = step
    if (b > 255):
        r = 0
        g = 0
        b = 255
        dr = step
        dg = 0
        db = -step


screen = Screen()
screen.bgcolor("black")
screen.colormode(255)


for i in range(100):
    colorshift()
    t.pencolor((r, g, b))
    t.fd(random()*30+100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.setpos(0, 0)  # sætter turtle tilbage til start men beholder retning
    t.left(12)


t.getscreen().exitonclick()

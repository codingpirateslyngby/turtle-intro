from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.colormode(255)

t= Turtle()
# t.pensize(5)
t.pencolor("red")
t.forward(100)
t.left(90)
t.pencolor("blue")
t.forward(100)
t.left(90)
t.pencolor("green")
t.forward(100)
t.left(90)
t.pencolor("yellow")
t.forward(100)
t.left(90)

screen.exitonclick()

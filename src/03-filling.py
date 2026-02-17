from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")

t= Turtle()
t.color("yellow")  # color of the line
t.fillcolor("green")
t.begin_fill()
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.end_fill()


screen.exitonclick()

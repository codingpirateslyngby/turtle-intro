from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")

t = Turtle()
t.hideturtle()
t.color("yellow") #color of the line
t.fillcolor("green") #color of the fill
t.begin_fill()

for i in range(24):
    t.forward(30)
    t.left(15)

t.end_fill()
screen.exitonclick()

from turtle import Turtle, Screen

lst = []

t = Turtle()
for i in range(5):
    lst.append(t.clone())
    t.left(60)
lst.append(t)


def drawPath():
    for turtle in lst:
        turtle.forward(10)
        turtle.right(10)


for i in range(36):
    drawPath()

t.getscreen().exitonclick()
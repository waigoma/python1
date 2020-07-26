import turtle
import random

turtle = turtle.Pen()


def random_walk(t, length, upper_x, upper_y, n):
    t.penup()
    t.goto(upper_x, upper_y)
    t.pendown()
    for i in range(n):
        r = random.randint(0, 360)
        t.right(r)
        t.forward(length)


random_walk(turtle, 50, 0, 0, 100)
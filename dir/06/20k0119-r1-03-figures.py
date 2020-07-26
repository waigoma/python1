import turtle

turtle = turtle.Pen()


def draw_triangle(t, length, upper_x, upper_y):
    t.penup()
    t.goto(upper_x, upper_y)
    t.pendown()
    for i in range(3):
        t.right(120)
        t.forward(length)


def draw_pentagon(t, length, upper_x, upper_y):
    t.penup()
    t.goto(upper_x, upper_y)
    t.pendown()
    for i in range(5):
        t.left(72)
        t.forward(length)


def draw_star(t, length, upper_x, upper_y):
    t.penup()
    t.goto(upper_x, upper_y)
    t.pendown()
    for i in range(5):
        t.right(144)
        t.forward(length)


draw_triangle(turtle, 100, -300, 100)
draw_pentagon(turtle, 100, 0, 100)
draw_star(turtle, 100, 300, 100)

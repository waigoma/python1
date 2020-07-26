import turtle

turtle = turtle.Pen()


def draw_rect(t, width, height, upper_left_x, upper_left_y):
    t.penup()
    t.goto(upper_left_x, upper_left_y)
    t.pendown()
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)


for x in range(10):
    x += 1
    draw_rect(turtle, 30*x, 30*x, -15*x, 15*x)

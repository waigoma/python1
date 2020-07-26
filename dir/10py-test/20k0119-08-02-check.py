import turtle

t = turtle.Turtle()
t.speed(0)

width = 50
a = 11
b = 11


def draw_square(turt, size):
    turt.pendown()
    turt.begin_fill()
    for i in range(4):
        turt.forward(size)
        turt.left(90)
    turt.end_fill()


for x in range(a):
    for y in range(b):
        if (x + y) % 2 == 0:
            color = t.color((1.0, 1.0, 1.0))
        else:
            color = t.color((0.0, x / a, y / b))
        t.penup()
        t.goto((x - 6) * width, (y - 6) * width)
        draw_square(t, width)

turtle.Screen().exitonclick()
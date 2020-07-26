import turtle

t = turtle.Turtle()
t.speed(-1)

t.penup()
t.goto(0, 200)
t.pendown()

t.fillcolor('yellow')
t.begin_fill()
for i in range(6):
    t.left(60)
    t.forward(50)
    t.right(60)
    t.circle(20)
    t.left(60)
    t.right(120)
    t.forward(50)
t.end_fill()

turtle.Screen().exitonclick()

import turtle

t = turtle.Turtle()
t.speed(-1)

i = int(input("花びらの枚数を入力(3以上)>>>"))

t.color('red')

t.fillcolor('pink')
t.begin_fill()

if i >= 3:
    for x in range(i):
        t.forward(50)
        t.right(135)
        t.forward(25)
        t.left(90)
        t.forward(25)
        t.right(135)
        t.forward(50)
        t.left(180 * (i - 2) / i)

t.end_fill()

turtle.Screen().exitonclick()
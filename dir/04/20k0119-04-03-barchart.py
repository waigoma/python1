import turtle

t = turtle.Pen()
t.penup()
t.setx(-200)
t.pendown()

i = input("棒グラフの値を入力")
list1 = eval(i)

length = len(list1)

for x in list1:
    t.forward(10)
    t.left(90)
    t.forward(x)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(x)
    t.left(90)

t.forward(10)
t.setx(-200)

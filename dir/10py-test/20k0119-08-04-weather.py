import turtle


temperatures = [[21, 17.7], [26.1, 19.4], [29.3, 21.2], [28.4, 21], [29.4, 20.9], [28.1, 20.7], [27.3, 19.8], [28.9, 20], [29.5, 21.4], [29.5, 22.2], [28.6, 22.9], [30.7, 22.9], [25.3, 20], [25.6, 20.4], [31.9, 22.1], [29.7, 22.9], [28.8, 20.8], [24.7, 19.7], [19.7, 18.1], [28.3, 18.1], [24.4, 19], [21.9, 17.9], [27.9, 18.7], [25.7, 20.4], [23.7, 18.5], [32.3, 20.4], [29.5, 23.3], [25.4, 20.6], [29.2, 20.3], [27.4, 22.3]]


t = turtle.Turtle()
t.speed(-1)


def draw_def_graph(t):  # 初期グラフ作成 x軸:1刻み, y軸:5刻み
    t.penup()
    t.goto(-450, -350)
    t.pendown()
    t.goto(460, -350)
    t.penup()
    t.goto(-400, 410)
    t.pendown()
    t.goto(-400, -400)
    t.penup()
    t.goto(-400, -350)
    t.pendown()
    # for x in range(30):
    #     t.forward(28.3)
    #     t.right(90)
    #     t.forward(10)
    #     t.forward(-20)
    #     t.forward(10)
    #     t.left(90)
    t.penup()
    t.goto(-400, -350)
    t.pendown()
    t.left(90)
    # for y in range(6):
    #     t.forward(100)
    #     t.right(90)
    #     t.forward(10)
    #     t.forward(-20)
    #     t.forward(10)
    #     t.left(90)
    t.penup()
    t.goto(-400, -350)
    t.pendown()
    t.right(90)


def draw_graph(t, max_temp, min_temp):
    t.forward(10)
    t.color('red')
    t.fillcolor('red')
    t.begin_fill()
    t.left(90)
    t.forward(max_temp * 10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(max_temp * 10)
    t.left(90)
    t.end_fill()
    t.color('black')
    t.forward(4)
    t.color('blue')
    t.fillcolor('blue')
    t.begin_fill()
    t.left(90)
    t.forward(min_temp * 10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(min_temp * 10)
    t.left(90)
    t.end_fill()
    t.color('black')


draw_def_graph(t)
for i in temperatures:
    draw_graph(t, i[0], i[1])


turtle.Screen().exitonclick()

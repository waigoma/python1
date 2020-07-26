import turtle

temperatures = [12.6, 6.5, 12.1, 12.1, 8.6, 11.1,
                10.0, 2.6, 3.2, 5.3, 8.2, 8.4, 10.0,
                8.6, 12.1, 8.8, 13.0, 6.8, 10.4, 13.6,
                17.4, 11.2, 11.9, 14.0, 14.6, 12.4, 13.3]

turtle = turtle.Pen()


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
    for x in range(30):
        t.forward(28.3)
        t.right(90)
        t.forward(10)
        t.forward(-20)
        t.forward(10)
        t.left(90)
    t.penup()
    t.goto(-400, -350)
    t.pendown()
    t.left(90)
    for y in range(6):
        t.forward(100)
        t.right(90)
        t.forward(10)
        t.forward(-20)
        t.forward(10)
        t.left(90)
    t.penup()
    t.goto(-400, -350)
    t.pendown()
    t.right(90)


def plot(t, temp_list):  # 気温ごとのプロット。y軸は5℃ごとに100, x軸は1日ごとに28.3
    x = -400
    z = 0
    for i in temp_list:
        x += 28.3
        y = i * 100 / 5 - 350
        if z == 0:
            t.penup()
            t.goto(x, y)
            t.pendown()
        t.goto(x, y)
        z += 1


draw_def_graph(turtle)
plot(turtle, temperatures)

from tkinter import *
# import turtle

x = 0
y = 0

tk = Tk()
canvas = Canvas(tk, width=400, height=300)
canvas.pack()


def on_click(event):
    global x
    global y

    x1 = event.x
    y1 = event.y
    canvas.create_rectangle(x1, y1, x, y)
    x = x1
    y = y1
    # print(f"({x}, {y})")


canvas.bind("<Button-1>", on_click)

# turtle.Screen().exitonclick()

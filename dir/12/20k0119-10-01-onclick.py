from tkinter import *
# import turtle


tk = Tk()
canvas = Canvas(tk, width=400, height=300)
canvas.pack()


def on_click(event):
    x = event.x
    y = event.y
    canvas.create_rectangle(x, y, x - 10, y - 10)
    # print(f"({x}, {y})")


canvas.bind("<Button-1>", on_click)

# turtle.Screen().exitonclick()

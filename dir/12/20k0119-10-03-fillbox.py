from tkinter import *
# import turtle

i = 0

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()


def on_click(event):
    global i
    a = 200
    b = 200
    r = 100
    x = event.x
    y = event.y
    if (x - a)**2 + (y - b)**2 < r**2:
        if i == 0:
            canvas.create_arc(100, 100, 300, 300, extent=359, style=CHORD, fill="red")
            i += 1
        elif i == 1:
            canvas.create_arc(100, 100, 300, 300, extent=359, style=CHORD, fill="green")
            i += 1
        elif i == 2:
            canvas.create_arc(100, 100, 300, 300, extent=359, style=CHORD, fill="blue")
            i = 0


canvas.create_arc(100, 100, 300, 300, extent=359, style=CHORD, fill="red")

canvas.bind("<Button-1>", on_click)

# turtle.Screen().exitonclick()

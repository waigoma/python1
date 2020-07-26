import turtle

t = turtle.Pen()

# for x in range(4):
#     t.forward(50)
#     t.right(90)
#     t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.right(90)

# for x in range(5):
#     t.forward(50)
#     t.right(135)
#     t.forward(25)
#     t.left(90)
#     t.forward(25)
#     t.right(135)
#     t.forward(50)
#     t.left(108)


max_temps = [21, 26.1, 29.3, 28.4, 29.4, 28.1, 27.3, 28.9, 29.5, 29.5, 28.6, 30.7, 25.3, 25.6, 31.9, 29.7, 28.8, 24.7,
             19.7, 28.3, 24.4, 21.9, 27.9, 25.7, 23.7, 32.3, 29.5, 25.4, 29.2, 27.4]

min_temps = [17.7, 19.4, 21.2, 21, 20.9, 20.7, 19.8, 20, 21.4, 22.2, 22.9, 22.9, 20, 20.4, 22.1, 22.9, 20.8, 19.7, 18.1,
             18.1, 19, 17.9, 18.7, 20.4, 18.5, 20.4, 23.3, 20.6, 20.3, 22.3]

temps = []

for i in range(len(max_temps)):
    temps.append([max_temps[i], min_temps[i]])
print(temps)
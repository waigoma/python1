import turtle

script = []

t = turtle.Pen()

with open(r"script.txt", encoding="utf-8_sig") as file:
    for line in file:
        line = line.rstrip("\n")
        fields = line.split(":")
        script.append([fields[0], fields[1]])

# print(script)

for t_move in script:
    # print(t_move)
    if t_move[0] == "FORWARD":
        t.forward(int(t_move[1]))
    elif t_move[0] == "LEFT":
        t.left(int(t_move[1]))
    elif t_move[0] == "RIGHT":
        t.right(int(t_move[1]))


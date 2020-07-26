# i = int(input("aaaaaa"))
# for x in range(i):
#     print(f"残り{5-x}")
# print("fin.")

# for x in range(3):
#     for y in range(3):
#         print(f"(x, y):({x}, {y})")

# values = [10, 20, 30]
# for x in values:
#     print(x)

# i = input("list>")
# values = eval(i)
# for x in values:
#     if x < 10:
#         print("ok")
#     else:
#         print("ng")

# i = input("list>")
# values = eval(i)
#
# current = values[0]
# for x in values:
#     if x > current:
#         current = x
# print(f"max: {current}")

# i = input("list>")
# values = eval(i)
#
# current = 0
# value = 0
# for x in values:
#     current += 1
#     value += x
# print(value/current)

i = input("list>")
values = eval(i)

current = values[0]
for x in values:
    if x < current:
        current = x
print(current)
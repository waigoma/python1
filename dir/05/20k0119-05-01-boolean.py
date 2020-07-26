def has_negative(x):
    for i in x:
        if i < 0:
            return True
    return False


i = input("list>")

values = eval(i)

if has_negative(values):
    print("has negative")
else:
    print("doesn't have negative")

value = 0

print("リストの数は必ず同じにしてください。")
i = input("list1>")
list1 = eval(i)

i = input("list2>")
list2 = eval(i)

length1 = len(list1)
length2 = len(list2)

if length1 == length2:
    for x in range(length1):
        value += list1[x] * list2[x]
    print(value)
else:
    print("リストの個数が違います。")
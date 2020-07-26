def find(list1, n):
    index_list = []
    index_num = 0
    for y in list1:
        if y == n:
            index_list.append(index_num)
        index_num += 1
    return index_list


i = input("list>")
x = int(input("どの数値を探すか>"))

values = eval(i)

index = find(values, x)

if len(index) == 0:
    print(f"{x}はリストに存在しない。")
else:
    print(f"{x}はリストの{index}番目に存在する。")

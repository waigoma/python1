def reverse(list1):
    length = len(list1)
    reverse_list = []
    for i in range(length):
        length -= 1
        reverse_list.append(list1[length])
    return reverse_list


i = eval(input("list>"))

print(f"list{i}を反転した結果\n→{reverse(i)}")
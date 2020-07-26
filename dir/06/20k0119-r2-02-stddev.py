import math


def average(lists):
    length = len(lists)
    sum_list = 0
    for x in lists:
        sum_list += x
    return sum_list / length


def deviation(lists, ave):
    length = len(lists)
    sum_list = 0
    for x in lists:
        sum_list += (x - ave) ** 2
    dispersion = sum_list / length
    return math.sqrt(dispersion)


num_list = eval(input("数値のリストを入力>>"))

print(f"リスト{num_list}\n平均値: {average(num_list)}\n標準偏差: {deviation(num_list, average(num_list))}")

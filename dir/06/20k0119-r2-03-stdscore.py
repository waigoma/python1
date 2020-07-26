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


def deviation_value(lists, ave, devi):
    for x in lists:
        print(f"点数{x}の偏差値は{(x - ave) / devi * 10 + 50}です。")


num_list = eval(input("数値のリストを入力>>"))

deviation_value(num_list, average(num_list), deviation(num_list, average(num_list)))

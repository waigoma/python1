temperatures = [12.6, 6.5, 12.1, 12.1, 8.6, 11.1,
                10.0, 2.6, 3.2, 5.3, 8.2, 8.4, 10.0,
                8.6, 12.1, 8.8, 13.0, 6.8, 10.4, 13.6,
                17.4, 11.2, 11.9, 14.0, 14.6, 12.4, 13.3]


def min_max(temp):
    minimum = 1000
    maximum = -1000

    for t in temp:
        # 最小値
        if t < minimum:
            minimum = t
        # 最大値
        if t > maximum:
            maximum = t
    return minimum, maximum


def average(temp):
    s = 0
    size = len(temp)

    for a in temp:  # 合計
        s += a
    return s / size  # return平均値


def graph(temp):
    for x in temp:
        print("*" * int(x) + f"{x}")


print(f"最低気温, 最高気温 = {min_max(temperatures)}\n平均気温 = {average(temperatures)}\nヒストグラム")
graph(temperatures)
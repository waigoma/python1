# aa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

i = input("入れ子リスト入力>")
aa = eval(i)

x = 0  # 入れ子リスト番号

maximum = 0  # 一番大きい数
maxList_i = 0  # 一番大きい数入りリスト番号

minimum = 0  # 一番小さい数
minList_i = 0  # 一番小さい数入りリスト番号

# 入れ子リスト処理
for a in aa:
    # リスト処理
    for y in a:
        # 最小
        if minimum > y:
            minimum = y
            minList_i = x

        # 最大
        if maximum < y:
            maximum = y
            maxList_i = x
    x += 1  # 入れ子リスト次へ

print(f"maxList: {aa[maxList_i]}\nminList: {aa[minList_i]}")

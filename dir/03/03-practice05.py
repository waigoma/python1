print("ループ処理をするには？\n(1) if文\n(2) for文\n(3) 辞書")
point = int(input())

if point == 2:
    print("正解")
elif point == 1 or point == 3:
    print("不正解")
else:
    print("無効")

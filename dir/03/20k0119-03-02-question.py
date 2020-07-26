print("ループ処理をするには？\n(a) if文\n(b) for文\n(c) 辞書")
point = input()

if point == "b":
    print("正解")
elif point == "a" or point == "c":
    print("不正解")
else:
    print(f"入力された選択肢({point})は正しくありません。")

print("一番面積の大きい国は？\n(a) アメリカ\n(b) 中国\n(c) ロシア")
point = input()

if point == "c":
    print("正解")
elif point == "a" or point == "b":
    print("不正解")
else:
    print(f"入力された選択肢({point})は正しくありません。")

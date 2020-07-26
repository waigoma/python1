dictionary = {"apple": "りんご", "grape": "ぶどう", "peach": "もも", "orange": "オレンジ", "cherry": "さくらんぼ", "strawberry": "いちご"}

print("知りたい単語を入力！")

str = input()
print(f"{str}が入力")

if str in dictionary:
    str1 = dictionary[str]
    print(str + ": " + str1)
else:
    print("この辞書にその言葉はない。どんまい。")


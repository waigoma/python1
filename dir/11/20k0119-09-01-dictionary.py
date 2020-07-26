dictionary = {}
key_list = []
value_list = []

with open(r"dictionary.txt", encoding="utf-8_sig") as file:
    for line in file:
        line = line.rstrip("\n")
        fields = line.split(":")
        key_list.append(fields[0])
        value_list.append(fields[1])

dictionary = dict(zip(key_list, value_list))


while True:
    i = input("知りたい言葉>>")

    if i == "fin":
        print("終了します...")
        break

    if i in dictionary:
        print(f"{i}の意味: {dictionary[i]}")
    else:
        print(f'"{i}"はこの辞書にありません。')

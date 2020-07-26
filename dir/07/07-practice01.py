# with open(r"file/example.txt", encoding="utf-8_sig") as file:
#     print(file.readline().rstrip("\n"))
#     print(file.readline().rstrip("\n"))
#     print(file.readline().rstrip("\n"))

# with open(r"file/numbers.txt", encoding="utf-8_sig") as file:
#     a = int(file.readline())
#     b = int(file.readline())
#     print(a + b)

# line = "2015/4/1, 13.9, 8, 1"
# fields = line.split("/")
# print(fields)

# with open(r"file/numbers.txt", encoding="utf-8_sig") as file:
#     a = float(file.readline())
#     b = float(file.readline())
#     print(a + b)

# line = input("日付>>")
# fields = line.split("/")
# print(fields[0]+"年"+fields[1]+"月"+fields[2]+"日")

# with open(r"file/example.txt", encoding="utf-8_sig") as file:
#     for line in file:
#         sline = line.rstrip("\n")
#         print(f"行: {sline}")

# with open(r"file/numbers.txt", encoding="utf-8_sig") as file:
#     total = 0
#     i = 0
#     for num in file:
#         total += float(num)
#         i += 1
#     print(total/i)

# with open(r"file/target.txt", encoding="utf-8_sig", mode="w") as file:
#     file.write("Hello world!日本語\n")
#     file.write(str(100))
li = eval(input("list>>"))

with open(r"file/target.txt", encoding="utf-8_sig", mode="w") as file:
    for list_num in li:
        file.write(str(list_num)+"\n")
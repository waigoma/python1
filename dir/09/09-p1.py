# with open("numbersH.txt", encoding="utf8") as file:
#     total = 0
#     line = file.readline()
#     line = line.rstrip()
#     field = line.split(",")
#     for x in field:
#         total += int(x)
#     print(f"平均値: {total / len(field)}")


# with open("numbersH.txt", encoding="utf8") as file:
#     total = 0
#     count = 0
#     lists = []
#     for line in file:
#         line = line.rstrip()
#         lists.append(line.split(","))
#     for x in lists:
#         for y in x:
#             count += 1
#             total += int(y)
#     print(f"平均値: {total / count}")


# values = [10, 20, 30]
# for i in values:
#     with open("numbersH.txt", encoding="utf8", mode="a") as file:
#         file.write(str(i * 2)+"\n")


values = ["10, 20, 30", "40, 50, 60", "70, 80, 90"]
for i in values:
    total = 0
    i = i.split(",")
    for x in i:
        total += int(x)
    with open("numbersH.txt", encoding="utf8", mode="a") as file:
        file.write(str(total)+"\n")

write_list = []

with open(r"06-extract-in.csv", encoding="utf-8_sig") as file:
    i = 0
    for line in file:
        i += 1
        if i == 4 or i > 5:
            line = line.rstrip("\n")
            fields = line.split(",")
            write_list.append([fields[0], fields[1]])

with open(r"06-extract-out.csv", encoding="utf-8_sig", mode="w") as file:
    for li in write_list:
        file.write(f"{li[0]},{li[1]}\n")
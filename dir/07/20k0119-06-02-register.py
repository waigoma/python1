sum_values = 0

with open(r"values.csv", encoding="utf-8_sig") as file:
    for line in file:
        line = line.rstrip("\n")
        fields = line.split(",")
        sum_values += int(fields[1]) * int(fields[2])

print(f"合計金額: {sum_values}")

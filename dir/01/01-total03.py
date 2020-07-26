price = 198
x = 12
tax = 0.1

total = price * x

print(f"小計:{total}円")
print(f"消費税:{total * tax}円")
print(f"合計:{total * (1 + tax)}円")

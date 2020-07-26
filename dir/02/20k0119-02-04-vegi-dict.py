price_list = {"りんご": 100, "オレンジ": 200, "ぶどう": 300}
tax = 1.08

print("りんご: " + str(price_list["りんご"]))
print("オレンジ: " + str(price_list["オレンジ"]))
print("ぶどう: " + str(price_list["ぶどう"]))

apple = price_list["りんご"]
orange = price_list["オレンジ"]
grape = price_list["ぶどう"]

A = apple * 1 + orange * 2 + grape * 3
B = orange * 2 + grape * 3
C = apple * 2 + orange * 4

print(f"Aさん : 税抜き {A} 円 \n 税込 {A * tax} 円")
print(f"Bさん : 税抜き {B} 円 \n 税込 {B * tax} 円")
print(f"Cさん : 税抜き {C} 円 \n 税込 {C * tax} 円")
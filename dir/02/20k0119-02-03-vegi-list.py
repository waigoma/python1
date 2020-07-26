goods_list = ["りんご", "オレンジ", "ぶどう"]
price_list = [100, 200, 300]
tax = 1.08

print(goods_list[0] + ": " + str(price_list[0]))
print(goods_list[1] + ": " + str(price_list[1]))
print(goods_list[2] + ": " + str(price_list[2]))

apple = price_list[0]
orange = price_list[1]
grape = price_list[2]

A = apple * 1 + orange * 2 + grape * 3
B = orange * 2 + grape * 3
C = apple * 2 + orange * 4

print(f"Aさん : 税抜き {A} 円 \n 税込 {A * tax} 円")
print(f"Bさん : 税抜き {B} 円 \n 税込 {B * tax} 円")
print(f"Cさん : 税抜き {C} 円 \n 税込 {C * tax} 円")
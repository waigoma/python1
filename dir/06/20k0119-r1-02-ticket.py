fare = {"静岡": [3350, 3300], "名古屋": [6260, 4620], "京都": [8210, 5390], "新大阪": [8750, 5390]}
money_list = []
name = ""
seat_name = ""

where = int(input("降車駅を選択→(1) 静岡, (2) 名古屋, (3) 京都, (4) 新大阪\n>>"))
if where == 1:
    money_list = fare["静岡"]
    name = "静岡"
elif where == 2:
    money_list = fare["名古屋"]
    name = "名古屋"
elif where == 3:
    money_list = fare["京都"]
    name = "京都"
elif where == 4:
    money_list = fare["新大阪"]
    name = "新大阪"
else:
    print("入力が不適切です。終了します。")
    exit()

seat_type = int(input("特急券の種別を選んでください。→(1) 指定席, (2) 自由席\n>>"))
if seat_type == 1:
    seat_name = "指定席"
elif seat_type == 2:
    seat_name = "自由席"
    money_list[1] = money_list[1] - 520
else:
    print("入力が不適切です。終了します。")
    exit()

print(f"東京から{name}まで\n運賃:{money_list[0]}円\n特急券({seat_name}):{money_list[1]}円\n合計:{money_list[0] + money_list[1]}円")
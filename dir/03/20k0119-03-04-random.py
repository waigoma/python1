import random

print("じゃんけん。\n1:グー\n2:チョキ\n3:パー")
i = int(input())

if 1 <= i <= 3:

# 自分の出した手
    if i == 1:
        print("グーを出した")
    elif i == 2:
        print("チョキを出した")
    else:
        print("パーを出した")

# 1から3をランダムで取得
    r = random.randint(1, 3)

# 判定(相子は負けとなる)
    if r == 1:  # vsグー
        print("相手はグーを出した")
        if i == 3:
            print("勝ち")
        else:
            print("負け")

    elif r == 2:  # vsチョキ
        print("相手はチョキを出した")
        if i == 1:
            print("勝ち")
        else:
            print("負け")

    else:  # vsパー
        print("相手はパーを出した")
        if i == 2:
            print("勝ち")
        else:
            print("負け")

else:
    print("無効な数値です。終了します。")

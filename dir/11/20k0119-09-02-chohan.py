import random

point = 10


def game_start(my_point):
    i = input("丁か半か宣言してください>>>")
    if i == "丁" or "半":
        game_point(i, my_point)
    else:
        print("不正な文字列です。再度入力してください。")
        game_start(my_point)


def game_point(which, my_point):
    p = int(input("賭けるポイント数を入力してください>>>"))
    if p > point or p < 0:
        print("不正なポイントまたはポイントを持っていません。もう一度入力してください。")
        game_point(which, my_point)
    else:
        print(f"{p}ポイント賭けました。ゲームを開始します。")
        random_dice(which, p, my_point)


def random_dice(which, p, my_point):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    s = a + b
    judge = ""

    if s == 2 or s == 4 or s == 6 or s == 8 or s == 10 or s == 12:
        judge = "丁"

    if s == 3 or s == 5 or s == 7 or s == 9 or s == 11:
        judge = "半"

    print(f"ダイスの目: {a}, {b}\n合計: {s}")

    if which == judge:
        print(f"よって判定は勝利！")
        cal_point(True, p, my_point)
    else:
        print(f"よって判定は敗北...")
        cal_point(False, p, my_point)


def cal_point(judge, p, my_point):
    if judge:
        my_point += p
    else:
        my_point -= p
    choice_continue(my_point)


def choice_continue(my_point):
    print(f"現在のあなたのポイント: {my_point}")
    if my_point > 0:
        i = input("まだゲームを続行しますか?(y/n)>>>")
        if i == "y":
            game_start(my_point)
        elif i == "n":
            print("終了します...")
            exit()
        else:
            print("不正な文字列です。もう一度入力してください。")
            choice_continue(my_point)
    else:
        print("ポイントが0になりました。終了します。")


game_start(point)

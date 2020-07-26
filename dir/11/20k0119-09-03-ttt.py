import random


board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


# 0→o 1→x


def judge(boards, count):
    draw = 0

    print("盤面↓")
    for n in boards:
        print(n)

    for b in boards:
        for number in b:
            if number == "-":
                draw += 1
    if (boards[0][0] == "o" and boards[0][1] == "o" and boards[0][2] == "o") or \
            (boards[1][0] == "o" and boards[1][1] == "o" and boards[1][2] == "o") or \
            (boards[2][0] == "o" and boards[2][1] == "o" and boards[2][2] == "o") or \
            (boards[0][0] == "o" and boards[1][0] == "o" and boards[2][0] == "o") or \
            (boards[0][1] == "o" and boards[1][1] == "o" and boards[2][1] == "o") or \
            (boards[0][2] == "o" and boards[1][2] == "o" and boards[2][2] == "o") or \
            (boards[0][0] == "o" and boards[1][1] == "o" and boards[2][2] == "o") or \
            (boards[0][2] == "o" and boards[1][1] == "o" and boards[2][0] == "o"):
        print("oの勝ち")
    elif (boards[0][0] == "x" and boards[0][1] == "x" and boards[0][2] == "x") or \
            (boards[1][0] == "x" and boards[1][1] == "x" and boards[1][2] == "x") or \
            (boards[2][0] == "x" and boards[2][1] == "x" and boards[2][2] == "x") or \
            (boards[0][0] == "x" and boards[1][0] == "x" and boards[2][0] == "x") or \
            (boards[0][1] == "x" and boards[1][1] == "x" and boards[2][1] == "x") or \
            (boards[0][2] == "x" and boards[1][2] == "x" and boards[2][2] == "x") or \
            (boards[0][0] == "x" and boards[1][1] == "x" and boards[2][2] == "x") or \
            (boards[0][2] == "x" and boards[1][1] == "x" and boards[2][0] == "x"):
        print("xの勝ち")
        exit()
    elif draw == 0:
        print("引き分け")
        exit()
    else:
        print("続行")
        if count == 0:
            play_o(boards)
        elif count == 1:
            play_x(boards)
        else:
            print("バグ発生。終了します...")
            print(boards)
            exit()


def play_o(boards):  # 人間先行
    print("----oのターン----")
    x = (int(input("何列目を変更しますか？>>>")) - 1)
    y = (int(input("何行目を変更しますか？>>>")) - 1)
    if (x == 0 or x == 1 or x == 2) and (y == 0 or y == 1 or y == 2):
        if boards[y][x] == "-":
            boards[y][x] = "o"
            judge(boards, 1)
        else:
            print("そこは変更不可能です。もう一度入力してください。")
            play_o(boards)
    else:
        print("無効な数字です。もう一度入力してください。")
        play_o(boards)


def play_x(boards):  # コンピュータ先行
    print("----xのターン----")
    # x = (int(input("何列目を変更しますか？>>>")) - 1)
    # y = (int(input("何行目を変更しますか？>>>")) - 1)
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if (x == 0 or x == 1 or x == 2) and (y == 0 or y == 1 or y == 2):
        if boards[y][x] == "-":
            boards[y][x] = "x"
            judge(boards, 0)
        else:
            # print("そこは変更不可能です。もう一度入力してください。")
            play_x(boards)
    else:
        # print("無効な数字です。もう一度入力してください。")
        play_x(boards)


def one_more(boards):
    inp = input("もう一度遊びますか?(y/n)>>>")
    if inp == "y":
        for x in range(0, 2):
            for y in range(0, 2):
                boards[x, y] = "-"
    elif inp == "n":
        print("終了します...")
        exit()

    which = int(input('先行が"あなた"の場合は1を、先行が"コンピュータ"の場合は2を入力してください。>>>'))
    if which == 1:
        play_o(boards)
    elif which == 2:
        play_x(boards)
    else:
        print("不正な文字列です。終了します。")
        exit()


i = int(input('3x3の"o""x"ゲームをスタートするには1を入力してください。>>>'))

if i == 1:
    first = int(input('先行が"あなた"の場合は1を、先行が"コンピュータ"の場合は2を入力してください。>>>'))
    if first == 1:
        play_o(board)
    elif first == 2:
        play_x(board)
    else:
        exit()
else:
    exit()

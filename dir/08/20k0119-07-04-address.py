from dataclasses import *
import os


@dataclass
class Address:
    name: str
    address: str
    number: str


filePath = "address.txt"


# アドレスを追加する関数。 名前があるかはexistsで判別。 あったら全行を読み込んで同じ名前の人の行を削除し、その行に新しい情報を入力
def add_address(address, nr, exists):
    with open(filePath, encoding="utf8") as addFile:
        if exists:
            l = addFile.readlines()  # 全行読み込み
            del l[nr]  # 特定行削除
            l.insert(nr, f"{address.name}, {address.address}, {address.number}\n")  # 特定行挿入

            with open(filePath, encoding="utf8", mode="w") as wFile:  # 上書きモードでファイルを開く
                wFile.writelines(l)  # 全部を上書き

        else:
            with open(filePath, encoding="utf8", mode="a") as wFile:  # 最終行挿入モードで開く
                wFile.write(f"{address.name}, {address.address}, {address.number}\n")  # 書き込み(最終行)


i = int(input("電話帳に追記する場合: 1、 一覧を閲覧する場合: 2、 終了する場合: 3、 を入力>>>"))

if os.path.isfile(filePath):  # 読み込もうとしているファイルは実際に存在するかどうか
    if i == 1:
        with open(filePath, encoding="utf-8_sig") as file:

            i = 0  # 現在の処理が何行目かカウント
            exist = False  # 同じ人の名前が出てきたかどうか
            n = 0  # もし出てきたら何行目で出たか

            inputName = input("追記したい人の名前を入力>>>")
            inputAddress = input("追記したい人のメールアドレスを入力>>>")
            inputNumber = input("追記したい人の電話番号を入力>>>")

            if inputName or inputAddress or inputNumber is None:
                print("必要情報が入力されていません。\n終了します...")
                exit()
            else:
                p_address = Address(inputName, inputAddress, inputNumber)  # クラスの情報にしとく

            for line in file:  # 1行ずつ読み込み
                line = line.rstrip("\n")
                fields = line.split(",")
                if fields[0] == inputName:  # 読み込んだ行の名前の欄とinputされた名前が同じか判別
                    print("true")
                    exist = True
                    n = i
                i += 1

            print(f"{exist}, {n}")
            add_address(p_address, n, exist)  # 最後に書き込みの処理

    elif i == 2:  # 全行出力するだけ
        if os.path.isfile(filePath):
            with open(filePath, encoding="utf-8_sig") as file:
                for line in file:
                    print(line.rstrip("\n"))

    elif i == 3:
        print("終了します...")
        exit()

    else:
        print("不正な文字列です。終了します...")
        exit()

else:
    print("ファイルが存在しません。\n終了します...")
    exit()

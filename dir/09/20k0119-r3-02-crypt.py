import os


def encryption(string):  # 暗号化
    n = 0
    pass_list = []
    for i in string:
        code = ord(i)
        if n == 2 * n:
            code += 1
        else:
            code -= 2
        n += 1
        pass_list.append(chr(code))
    return pass_list


def decryption(string):  # 復号化
    n = 0
    pass_list = []
    for i in string:
        code = ord(i)
        if n == 2 * n:
            code -= 1
        else:
            code += 2
        n += 1
        pass_list.append(chr(code))
    return pass_list


filePass = "pass.txt"
inp = int(input("暗号化: 1、 復号化: 2>>>"))

if inp == 1:
    password = input("暗号化したいパスワードを記入してください。>>>")
    if os.path.isfile(filePass):
        with open(filePass, encoding="utf8", mode="w") as file:
            file.write("".join(encryption(password)))
    else:
        print("ファイルが見つかりません。")
        exit()

elif inp == 2:
    print("復号化します。")
    password_list = []
    if os.path.isfile(filePass):
        with open(filePass, encoding="utf8") as file:
            for line in file:
                line = line.rstrip()
                print("".join(decryption(line)))
    else:
        print("ファイルが見つかりません。")
        exit()

else:
    print("不正な文字列です。")
    exit()

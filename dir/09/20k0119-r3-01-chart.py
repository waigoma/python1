import math
import time
import turtle
from dataclasses import *

t = turtle.Pen()


@dataclass
class PersonalInfo:
    name: str
    math_score: int
    physics_score: int
    eng_score: int


def studentsInfo():
    return [PersonalInfo("Alice", 100, 65, 57), PersonalInfo("Bob", 45, 98, 100), PersonalInfo("Charley", 50, 50, 50)]


def highScores():
    math_name = ""
    physics_name = ""
    eng_name = ""
    maximum_math = 0
    maximum_physics = 0
    maximum_eng = 0
    for i in studentsInfo():
        if maximum_math < i.math_score:
            maximum_math = i.math_score
            math_name = i.name
        if maximum_physics < i.physics_score:
            maximum_physics = i.physics_score
            physics_name = i.name
        if maximum_eng < i.eng_score:
            maximum_eng = i.eng_score
            eng_name = i.name
    return [math_name, physics_name, eng_name]


def highScore():
    high_name = ""
    sum_test = 0
    for i in studentsInfo():
        score = i.math_score + i.physics_score + i.eng_score
        if score > sum_test:
            sum_test = score
            high_name = i.name
    return high_name


def radar_chart(stu, point):
    for i in stu:
        if i.name == point:
            t.penup()
            t.goto((200 * math.sin(2 * math.pi / 3)), 200 * math.cos(2 * math.pi / 3))
            t.pendown()
            t.goto((200 * math.sin(4 * math.pi / 3)), 200 * math.cos(4 * math.pi / 3))
            t.goto((200 * math.sin(6 * math.pi / 3)), 200 * math.cos(6 * math.pi / 3))
            t.goto((200 * math.sin(2 * math.pi / 3)), 200 * math.cos(2 * math.pi / 3))
            t.color("red")
            t.penup()
            t.goto((2 * i.math_score * math.sin(2 * math.pi / 3)), 2 * i.math_score * math.cos(2 * math.pi / 3))
            t.pendown()
            t.goto((2 * i.physics_score * math.sin(4 * math.pi / 3)), 2 * i.physics_score * math.cos(4 * math.pi / 3))
            t.goto((2 * i.eng_score * math.sin(6 * math.pi / 3)), 2 * i.eng_score * math.cos(6 * math.pi / 3))
            t.goto((2 * i.math_score * math.sin(2 * math.pi / 3)), 2 * i.math_score * math.cos(2 * math.pi / 3))
            time.sleep(10)


i = input("誰のレーダーチャートが見たいですか？>>>")
radar_chart(studentsInfo(), i)
# print(f"数学最高得点者: {highScores()[0]}, 物理最高得点者: {highScores()[1]}, 英語最高得点者: {highScores()[2]}")
# print(f"最高合計得点者: {highScore()}")

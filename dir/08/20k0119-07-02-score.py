from dataclasses import *


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


print(f"数学最高得点者: {highScores()[0]}, 物理最高得点者: {highScores()[1]}, 英語最高得点者: {highScores()[2]}")
print(f"最高合計得点者: {highScore()}")

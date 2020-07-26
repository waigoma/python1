# 問題1
from dataclasses import *


@dataclass
class Rect:
    x: int
    y: int
    width: int
    height: int


# 問題2
def area_rect(rect):
    return abs(rect.width * rect.height)


# 問題3
def map_area_rect(rects):
    results = []
    for x in rects:
        results.append(abs(x.width * x.height))
    return results


rectangles = [Rect(0, 0, 2, 4), Rect(0, 0, 4, 4), Rect(0, 0, 3, 2)]
print(map_area_rect(rectangles))


# 問題4
def filter_rect_20(rects):
    results = []
    for x in rects:
        if abs(x.width * x.height) > 20:
            results.append(x)
    return results


print(filter_rect_20(rectangles))


# 問題5
def fold_plus(rects):
    result = 0
    for x in rects:
        result += x
    return result


print(fold_plus(map_area_rect(rectangles)))

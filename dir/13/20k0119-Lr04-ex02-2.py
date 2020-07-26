from dataclasses import *


@dataclass
class Rect:
    x: int
    y: int
    width: int
    height: int


# 問題1
def includes_point(r, x, y):
    if r.x < x < r.x + r.width and r.y < y < r.height:
        return True
    else:
        return False


print(includes_point(Rect(0, 0, 2, 2), 1, 1))
print(includes_point(Rect(0, 0, 2, 2), 3, 3))


# 問題2
def includes_rect(r1, r2):
    if (abs(r1.x) > abs(r2.x) and r1.x + r1.width > r2.x + r2.width) and (abs(r1.y) > abs(r2.y) and r1.y + r1.height > r2.y + r2.height):
        return True
    else:
        return False


r1 = Rect(-1, -1, 4, 4)
r2 = Rect(0, 0, 2, 2)
print(includes_rect(r1, r2))

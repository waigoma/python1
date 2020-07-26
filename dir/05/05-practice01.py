# i = [3, 4, 5, 6, 7]
#
# a = sum(i)/len(i)
#
# print(a)

# score = int(input())
# x = max(0, score)
#
# print(x)


# def plus1(a):
#     return a + 1
#
#
# print(plus1(100))


# def myAbs(a):
#     if a < 0:
#         a *= -1
#     return a
#
#
# print(myAbs(500))


# def mySum(a):
#     result = 0
#     for x in a:
#         result += x
#     return result
#
#
# print(mySum([1, 2, 3, 4, 5, 6]))


# def myMax(a, b):
#     if a > b:
#         return a
#     return b
#
#
# print(myMax(10, 2))


# def myPrint(string, n):
#     for i in range(n):
#         print(string)
#
#
# myPrint("aaaaaa", 10)


def f1(a):
    print(locals())


def f2(b):
    print(locals())


f1(10)
f2(20)
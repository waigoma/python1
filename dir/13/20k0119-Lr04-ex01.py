# 問題1
def map_square(values):
    results = []
    for x in values:
        results.append(x ** 2)
    return results


v = [1, 2, -1, -2]
print(map_square(v))


# 問題2
def filter_positive(values):
    results = []
    for x in values:
        if x > 0:
            results.append(x)
    return results


v = [1, 2, -1, -2]
print(filter_positive(v))


# 問題3
def sum_square(values):
    result = 0
    for x in values:
        result += x ** 2
    return result


v = [1, -2, 3, -4, 5]
print(f"result = {sum_square(v)}")


# 問題4
def count_positive(values):
    count = 0
    for x in values:
        if x > 0:
            count += 1
    return count


v = [1, -2, 3, -4, 5]
print(f"result = {count_positive(v)}")

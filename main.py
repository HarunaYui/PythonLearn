import Lesson1


def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n


if __name__ == '__main__':
    data = [1, 2, 3, 5, 8, 6, 4, 10, 12, 1, 2, 1, 2, 3, 1]
    target = 1
    n = count(data, target)
    print(n)

    # R-1.1
    n = 20
    m = 10
    result1 = Lesson1.is_multiple(n, m)
    print(result1)

    # R-1.2
    k = 20
    result2 = Lesson1.is_even(k)
    print(result2)

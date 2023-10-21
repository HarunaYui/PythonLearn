# 按装订区域中的绿色按钮以运行脚本。

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

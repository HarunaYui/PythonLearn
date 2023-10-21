def is_multiple(n, m):
    i = 2
    if n == m * i:
        return True
    else:
        return False


# B养的不让用乘法,除法和取余.温柔是你的美
def is_even(k):
    odd = ['1', '3', '5', '7', '9']
    i = 0
    str_i = str(k)
    length = len(str_i)
    while i < length:
        if i != length - 1:
            i = i + 1
            continue
        for n in odd:
            if n == str_i[i]:
                return False
            else:
                return True

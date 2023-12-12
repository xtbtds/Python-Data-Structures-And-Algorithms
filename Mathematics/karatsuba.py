def length(x):
    n = 0
    if x <= 1: # Пришлось отдельно обрабатывать 0 и 1, т.к. битовый сдвиг дает 0
        return 1
    while x > 1:
        x >>= 1
        n += 1
    return n


def two_halfs(a, n):
    x = a
    half_n = n >> 1
    x_l = a >> (half_n)
    x_r = a & ((1 << half_n) - 1)
    return x_l, x_r


def karatsuba(x, y):
    n = max(length(x), length(y))
    if n == 1:
        return x * y
    half_n = n >> 1
    x_l, x_r = two_halfs(x, n)
    y_l, y_r = two_halfs(y, n)
    p1 = karatsuba(x_l, y_l)
    p2 = karatsuba(x_r, y_r)
    p3 = karatsuba(x_l + x_r, y_l + y_r)
    return (p1 << 2 * half_n) + ((p3 - p1 - p2) << half_n) + p2


res = karatsuba(9874563256487921, 152458796389852357456)

print(res)

def multiply(a, b):
    if not b:
        return 0
    c = multiply(a, b >> 1)
    return a + (c << 1) if b & 1 else c << 1


print(multiply(11, 13))  # 143

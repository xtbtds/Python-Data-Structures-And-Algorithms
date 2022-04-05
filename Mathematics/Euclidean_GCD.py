#finds greatest common divisor of 2 numbers
def gcd_div(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def gcd_recursive(a,b):
    if a == 0:
        return b
    return gcd_recursive(b % a, a)

def gcd_minus(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

if __name__ == "__main__":
    a = 36
    b = 128
    res1 = gcd_div(b,a)
    res2 = gcd_recursive(a,b)
    res3 = gcd_minus(a,b)
    print(res1, res2, res3)
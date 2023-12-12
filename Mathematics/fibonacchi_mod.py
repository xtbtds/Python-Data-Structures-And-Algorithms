def fib_mod(n, m):
    ost = [0,1]
    f0, f1 = 0, 1
    for _ in range(1, n):
        f0, f1 = f1, (f0+f1)%m
        if f1 == 0 and f1+(f0 % m) == 1:
            break
        ost.append(f1)
    return ost[n % len(ost)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()

#recursive implementation - O(2^n) time
def catalan_recursive(n):
    if n <= 1:
        return 1
    c = 0
    for i in range(n):
        c = c + catalan_recursive(i) * catalan_recursive(n-i-1)
    return c


#DP implementation - O(n^2) time
def catalan_dynamic(n):
    if n == 0 or n == 1:
        return 1
    catalan = [0] * (n+1)
    catalan[0] = 1
    catalan[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    return catalan[n]


#Binomial coefficient  - O(n) time
def binCoef(n, k):
    res = 1
    for i in range (k):
        res = res * (n-i)
        res = res / (n-k)
    return res
def catalan_bc(n):
    res = binCoef(2*n, n)
    res = res / (n+1)
    return res
    




def sieve_of_eratosthenes(n):
    numbers = [i for i in range(n+1)]
    """
    numbers - list of all numbers from 0 to n, we change the number to 0 if it is NOT prime
    1 is NOT prime, we start from 2
    """
    numbers[1] = 0
    i = 2
    while i <= n:
        if numbers[i] != 0:        #if its not 0, we've found prime
            j = i*2                #the first multiple for i
            while j <= n:
                numbers[j] = 0     #all these multiples are NOT prime
                j += i
        i += 1
    primes = [i for i in numbers if i != 0]
    return primes


if __name__ == "__main__":
    n = 29
    res = sieve_of_eratosthenes(n)
    print(res)


        



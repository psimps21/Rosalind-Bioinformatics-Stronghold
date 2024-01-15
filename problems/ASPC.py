import numpy as np
import math
import sys

def ReadFromFile(input_f):
    with open(input_f, 'r') as f:
        line = f.readline()

    n, m = line.strip().split()
    # print(n,m)
    
    # n = int(data[0].strip())

    return int(n), int(m)


def factorial(n):
    total = 1
    for i in range(2,n+1):
        # print(i)
        # total += np.log(i)
        total *= i % 1e6
    
    # print(f'{n} factorial is {np.exp(total)}')

    return total % 1e6
    # return np.round(np.exp(total))


def SumCombinations(n,m):
    num, denom = 0,0
    for i in range(m+1,n+1):
        num += np.log(i)

    for j in range(1,m+1):
        pass

    return

def Combination(n,k):
    if n == k or n == 0:
        return 1
    elif n - k == 1 or k == 1:
        return n
    
    num = 1.0
    for i in range(k+1,n+1):
        num *= i

    denom = 1.0
    for j in range(1, n-k+1):
        denom *= j

    print(num, denom)
    return np.exp(np.log(num) - np.log(denom))
    # return num / denom

# def Combination(n,k):
    # nm = np.math.factorial(n) % 1e6
    # km = np.math.factorial(k) % 1e6
    # nkm = np.math.factorial(n-k) % 1e6
    # nm = factorial(n)
    # km = factorial(k)
    # nkm = factorial(n-k)
    # return nm / (km * nkm)
    # return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))
    # return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))


# def AlternativeSplice(n,m):
#     total = 0
#     for i in range(m,n+1):
#         total += Combination(n,i) % 1e6
#         print(i, total)

    # p = (2**n) - (2**(m))
    # print((2**n),(2**(m)))
    # return int(total % 1e6)

def AlternativeSplice(n,m):
    total = 0
    for i in range(m,n+1):
        nCk = 1
        for j in range(1, i+1):
            nCk *= (n-j+1)
            nCk //= j
        total += nCk % 1e6
        # total += nCk
    return int(total % 1e6)


if __name__ == '__main__':
    input_f = sys.argv[1]

    n,m = ReadFromFile(input_f)
    print(n,m)

    sets = AlternativeSplice(n,m)

    print(f'There are {sets} sets')


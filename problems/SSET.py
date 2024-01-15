import numpy as np
import sys

def ReadFromFile(input_f):
    with open(input_f, 'r') as f:
        n = f.readline()

    # print(data)
    
    # n = int(data[0].strip())

    return int(n)

# def factorial(n):
#     return np.math.factorial(n)

def Combination(n,k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k))

def Subsets(n):
    total = 1

    for i in range(1,n+1):
        total += Combination(n,i)
        # print(total)
    
    return int(total) % 1000000


def Subsets2(n):
    return (2**n) % 1000000

if __name__ == '__main__':
    input_f = sys.argv[1]

    n = ReadFromFile(input_f)
    print(n)

    sets = Subsets(n)

    print(f'There are {sets} sets')


"""
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""
import sys, copy
import numpy as np

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        lines = f.readlines()
    
    n, m = [int(x) for x in lines[0].split(' ')]
    return n, m

def fib_mortal(n, m):
    if n == 1 or n == 2:
        return 1

    memo = [0, 1, 1]
    for i in range(3, n+1):
        if i <= m:
            result = memo[i-1] + memo[i-2]

        elif i == m+2 or i == m+1:
            result = memo[i-1] + memo[i-2] - 1

        else:
            result = memo[i-1] + memo[i-2] - memo[-(m+1)]
        memo.append(result)
        print(memo)

    return memo[-1]

# Solution found Rosalind user: abeliangrape
def fib(n, k=1):
    ages = [1] + [0] * (k - 1)
    for i in range(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)

if __name__ == '__main__':
    input_f = sys.argv[1]
    n,m = ReadInput(input_f)

    print(fib_mortal(n, m))

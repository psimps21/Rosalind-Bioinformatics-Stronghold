"""
Given: Positive integers n ≤ 40 and k ≤ 5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        lines = f.readlines()
    
    n, k = [int(x) for x in lines[0].split(' ')]
    return n, k

def fibSeq(n, k):
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1] + k * fib[i-2])
    return fib[n]


if __name__ == '__main__':
    input_f = sys.argv[1]
    n,k = ReadInput(input_f)

    print(fibSeq(n, k))

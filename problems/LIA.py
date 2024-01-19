"""
Given: Two positive integers k (k≤7) and N(N≤2^k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
Tom has two children in the 1st generation, each of whom has two children, and so on. 
Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N
 Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). 
 Assume that Mendel's second law holds for the factors.
"""
import sys
from math import factorial

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        data = f.readlines()
    
    k, n = [int(x) for x in data[0].strip().split()]

    return k, n

def hetorz_prob(k, n):
    total = 0
    for i in range(0, n):
        gen_num = 2**k
        comb = factorial(gen_num)/(factorial(gen_num-i)*factorial(i))
        total += comb * (.75**(gen_num-i)) * (.25**i)

    return round(1 - total, 3)


if __name__ == '__main__':
    input_f = sys.argv[1]
    k, n = ReadInput(input_f)
    
    print(hetorz_prob(k, n))

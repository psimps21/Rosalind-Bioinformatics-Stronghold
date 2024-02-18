"""
Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a
random string constructed with the GC-content found in A[k] will match s exactly.
"""
from math import log10
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        data = [x.strip() for x in f.readlines()]
    
    probs = [float(x) for x in data[1].split(' ')]
    return data[0], probs

def randomStrings(seq, prob_list):
    new_probs = []
    for prob in prob_list:
        base_prob = {
            'A': (1 - prob) / 2,
            'T': (1 - prob) / 2,
            'G': prob / 2,
            'C': prob / 2
        }

        new_prob = 0
        for base in seq:
            new_prob += log10(base_prob[base])

        new_probs.append(round(new_prob, 3))

    return new_probs


if __name__ == '__main__':
    input_f = sys.argv[1]
    seq, probs = ReadInput(input_f)
    print(*randomStrings(seq, probs))
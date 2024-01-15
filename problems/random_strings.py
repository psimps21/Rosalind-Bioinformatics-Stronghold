"""
Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a
random string constructed with the GC-content found in A[k] will match s exactly.
"""

from math import log10

def ran_strs(seq, prob_list):
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
    seq = input('Enter a DNA sequence: ')
    probs = input('Enter a series of probabilities separated by spaces: ').split(' ')
    probs = [float(i) for i in probs]
    print(*ran_strs(seq, probs))
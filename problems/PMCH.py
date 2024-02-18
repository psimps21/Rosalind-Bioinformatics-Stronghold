"""
Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number
of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
"""
from math import factorial
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as fasta:
        sequence_list = []

        for line in fasta.readlines():
            if line.startswith('>'):
                sequence_list.append('')

            else:
                sequence_list[-1] += line.strip('\n')
    
    return sequence_list[-1]

def p_matching(seq):
    return factorial(seq.count("A")) * factorial(seq.count("C"))

if __name__ == '__main__':
    input_f = sys.argv[1]
    seq = ReadInput(input_f)
    print(p_matching(seq))

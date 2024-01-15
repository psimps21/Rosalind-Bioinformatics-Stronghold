"""
Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number
of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
"""

from fasta_parser import FASTA
from math import factorial

def p_matching(seq):
    return factorial(seq.count("A")) * factorial(seq.count("C"))

if __name__ == '__main__':
    filename = input('Enter a file name: ')
    seqs, _ = FASTA(filename)
    seqs = list(seqs.values())
    print(p_matching(seqs[0]))

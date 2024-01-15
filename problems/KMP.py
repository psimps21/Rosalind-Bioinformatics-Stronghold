"""
Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
"""
import numpy as np
import sys
from Bio import SeqIO


def ReadFromFile(input_f):
    seqs = []
    with open(input_f, 'r') as f:
        for record in SeqIO.parse(f, 'fasta'):
            seqs.append(str(record.seq))

    return seqs[0]

def FailureArray(seq):
    return

if __name__ == '__main__':
    input_f = sys.argv[1]

    seqs = ReadFromFile(input_f)
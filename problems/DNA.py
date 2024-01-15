"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and
'T' occur in s.
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        lines = f.readlines()
    
    seq = lines[0]
    return seq

def nucleotide_count(seq):
    acgt_count = [0] * 4

    for base in seq:
        if base == "A":
             acgt_count[0] += 1
        elif base == "C":
             acgt_count[1] += 1
        elif base == "G":
             acgt_count[2] += 1
        elif base == "T":
             acgt_count[3] += 1

    return acgt_count


if __name__ == '__main__':
     input_f = sys.argv[1]
     seq = ReadInput(input_f)

     base_count = nucleotide_count(seq)
     print(*base_count)
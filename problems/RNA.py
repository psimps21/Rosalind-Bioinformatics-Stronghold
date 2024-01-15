"""
Given: A DNA string s
of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and
'T' occur in s
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        lines = f.readlines()
    
    seq = lines[0]
    return seq

def insertU(dna):
    """ Converts an DNA sequence to an RNA sequence """
    # PARAM [str] dna: the DNA sequence
    # RETURN [str]: the RNA sequence

    rna = dna.replace('T', 'U')

    return rna


if __name__ == '__main__':
    # seq = input('Input a DNA sequence: ')
    input_f = sys.argv[1]
    seq = ReadInput(input_f)
    
    print(insertU(seq))

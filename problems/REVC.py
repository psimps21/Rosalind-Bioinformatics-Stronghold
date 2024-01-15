"""
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        lines = f.readlines()
    
    seq = lines[0]
    return seq

def reverse_comp(forward):
    """ Generate the reverse complement of a sequence """
    # PARAM [str] forward: a sequence
    # RETURN [str]: the reverse complement of the forward sequence

    bases = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }

    reverse = ''

    # Generate the complementary strand
    for i in range(len(forward)):
        reverse = bases[forward[i]] + reverse

    # Return the reverse of the complement
    return reverse


def rev_comp(s):
    return s[::-1].translate(str.maketrans('ACGT', 'TGCA'))


if __name__ == '__main__':
    # seq = input('Enter a DNA sequence: ')
    input_f = sys.argv[1]
    seq = ReadInput(input_f)

    print()
    print(reverse_comp(seq))
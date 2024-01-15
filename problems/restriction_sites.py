"""
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return
these pairs in any order.
"""

from fasta_parser import FASTA

def rev_comp(forward):
    bases = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }

    reverse = ''

    # Generate the complementary strand
    for i in range(len(forward)):
        reverse += bases[forward[i]]

    # Return the reverse of the complement
    return reverse[::-1]

def find_reverse_comps(filename, min_len, max_len):
    seq, _ = FASTA(filename)
    seq = [str(s) for s in seq.values()][0]
    rcs = []

    for i in range(min_len, max_len+1):
        for j in range(0, len(seq)-i+1):
            if seq[j:j+i] == rev_comp(seq[j:j+i]):
                rcs.append((j+1, i))

    return rcs


if __name__ == '__main__':
    filename = input('Enter a file path: ')
    rcs = find_reverse_comps(filename, 4, 12)
    for rc in rcs:
        print(*rc)
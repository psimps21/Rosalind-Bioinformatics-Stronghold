"""
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions
exist, you may return any one.
"""

from fasta_parser import FASTA

def motif_indices(s, t):
    t_pos = 0
    indices = []

    for inx, base in enumerate(s):
        if base == t[t_pos]:
            indices.append(inx+1)
            t_pos += 1

        if t_pos == len(t):
            break

    return indices

if __name__ == '__main__':
    filename = input('Enter file path: ')
    seqs, order = FASTA(filename)
    indices = motif_indices(seqs[order[0]], seqs[order[1]])
    print(*indices)
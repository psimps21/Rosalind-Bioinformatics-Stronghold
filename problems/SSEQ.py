"""
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions
exist, you may return any one.
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as fasta:
        sequence_list = []

        for line in fasta.readlines():
            if line.startswith('>'):
                sequence_list.append('')

            else:
                sequence_list[-1] += line.strip('\n')
    
    return sequence_list[0], sequence_list[1]

def motif_indices(s, t):
    t_pos = 0
    indices = []

    inx = 0
    while len(indices) < len(t) and inx < len(s):
        if s[inx] == t[t_pos]:
            indices.append(inx+1)
            t_pos += 1

        inx += 1

    return indices

if __name__ == '__main__':
    input_f = sys.argv[1]
    s,t = ReadInput(input_f)

    indices = motif_indices(s,t)
    print(*indices)
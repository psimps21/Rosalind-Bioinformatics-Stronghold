"""
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
"""

from fasta_parser import FASTA

def tt_ratio(seqs):
    itions = {'A': 'G',
              'G': 'A',
              'C': 'T',
              'T': 'C'}

    t1, t2 = 0, 0 # transition, transversion

    for i in range(len(seqs[0])):
        if seqs[0][i] != seqs[1][i]:
            if seqs[0][i] == itions[seqs[1][i]]:
                t1 += 1
            else:
                t2 += 1

    return t1/t2


if __name__ == '__main__':
    filename = input('Enter a file name:')
    seqs, _ = FASTA(filename)
    seqs = list(seqs.values())
    print(tt_ratio(seqs))

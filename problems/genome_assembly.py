"""
Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads
deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire
chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
"""

from fasta_parser import FASTA

def superstring(seqs):
    supstrs = []
    mid = len(seqs[0]) // 2

    for seq in seqs:
        if len(supstrs) == 0:
            supstrs.append(seq)
            continue


def align

if __name__ == '__main__':
    p = [0,1,2]
    print(p[2:])
    # filename = input('Enter a file name: ')
    # seqs, _ = FASTA(filename)
    # seqs = list(seqs.values())



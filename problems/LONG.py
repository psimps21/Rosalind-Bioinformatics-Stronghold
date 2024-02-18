"""
Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which 
represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the 
entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
"""
import numpy as np
import sys
from Bio import SeqIO

def ReadFromFile(input_f):
    seqs = []
    with open(input_f, 'r') as f:
        for record in SeqIO.parse(f, 'fasta'):
            seqs.append(str(record.seq))

    return seqs


def SuffixPrefixSuperString(str1, str2):
    n1, n2 = len(str1), len(str2)

    # print(f'> {str1}\n', f'> {str2}\n')

    max_str1_sfx = 0
    max_str2_sfx = 0

    minn = np.min([n1,n2])
    half_min = minn // 2

    for i in range(half_min,minn+1):
        # Suffix prefix overlap of str1 and str2
        if str1.endswith(str2[:i]):
            max_str1_sfx = i

        if str2.endswith(str1[:i]):
            max_str2_sfx = i

    # If suffix prefix there is no overlap for either string
    if max_str1_sfx + max_str2_sfx == 0:
        return 0, ''
    # If equal overlaps or str1 has the longer overlap take the first str1 suffix 
    elif (max_str1_sfx == max_str2_sfx) or (max_str1_sfx > max_str2_sfx):
        return max_str1_sfx, str1 + str2[max_str1_sfx:]
    # if str2 has the longer overlap
    elif max_str1_sfx < max_str2_sfx:
        return max_str2_sfx, str2 + str1[max_str2_sfx:]
    

def ShortestSuperString(seqs):
    if len(seqs) == 1:
        return seqs[0]
    
    else:
        # 3 Shortest super string
        sss = seqs.pop(0)

        new_sss = ''
        counter = 0

        while len(new_sss) == 0 and counter < len(seqs):
            overlap, new_seq = SuffixPrefixSuperString(sss, seqs[counter])

            if overlap > 0:
                new_sss = new_seq

            else:
                counter += 1

        seqs.pop(counter)
        seqs = [new_sss] + seqs

        return ShortestSuperString(seqs)


# def ShortestSuperString(seqs):
#     stopper = 0
#     while len(seqs) > 1:
#         stopper += 1
#         print(stopper)

#         max_overlap = 0
#         best_seq = ''
#         x, y = -1, -1

#         for i in range(len(seqs)):
#             for j in range(i):
#                 overlap, new_seq = SuffixPrefixSuperString(seqs[i], seqs[j])
#                 if overlap > max_overlap:
#                     max_overlap = overlap
#                     best_seq = new_seq
#                     x, y = i, j

        
#         seqs.pop(x)
#         seqs.pop(y)
#         seqs.append(best_seq)
        
#     return seqs[0]


if __name__ == '__main__':
    input_f = sys.argv[1]

    seqs = ReadFromFile(input_f)

    sss = ShortestSuperString(seqs)

    print('Shortest Superstring is:',sss)


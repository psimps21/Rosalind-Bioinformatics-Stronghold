"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you
may return any one of them.)
"""
import numpy as np
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as fasta:
        sequence_list = []

        for line in fasta.readlines():
            if line.startswith('>'):
                sequence_list.append('')

            else:
                sequence_list[-1] += line.strip('\n')
    
    return sequence_list

def most_likely_common_ancestor(seq_list):
    profile_matrix = np.zeros((4, len(seq_list[0])), dtype=int)
    idx_map = {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }
    bases_map = {v:k for k,v in idx_map.items()}
    
    for seq in seq_list:
        for idx, nt in enumerate(seq):
            profile_matrix[bases_map[nt]][idx] += 1

    consensus_base_idxs = profile_matrix.argmax(axis=0)
    consensus_seq = ''.join([idx_map[idx] for idx in consensus_base_idxs])

    # Print the profile matrix
    print(consensus_seq)
    print('A:', *profile_matrix[0])
    print('C:', *profile_matrix[1])
    print('G:', *profile_matrix[2])
    print('T:', *profile_matrix[3])

    return consensus_seq


if __name__ == '__main__':
    input_f = sys.argv[1]
    seq_list = ReadInput(input_f)
    print()
    most_likely_common_ancestor(seq_list)

"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you
may return any one of them.)
"""

import numpy as np

def most_likely_common_ancestor(filename):
    seq_list = []
    sequence = ''
    with open(filename, 'r') as fasta:
        for line in fasta:
            if line[0] == '>':
                # Continue on first line of file
                if not sequence:
                    continue

                seq_list.append(sequence)
                sequence = ''
                continue

            line = line.replace('\n', '')
            sequence += line
    seq_list.append(sequence)

    profile_matrix = np.zeros((4, len(seq_list[0])), dtype=int)

    for inx in range(len(seq_list[0])):
        for seq in seq_list:
            if seq[inx] == 'A':
                profile_matrix[0][inx] += 1
            elif seq[inx] == 'C':
                profile_matrix[1][inx] += 1
            elif seq[inx] == 'G':
                profile_matrix[2][inx] += 1
            elif seq[inx] == 'T':
                profile_matrix[3][inx] += 1

    # Link profile matrix row indices to bases
    bases = {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }

    common_seq = ''
    for i in range(len(profile_matrix[0])):
        max_num = -1
        for j in range(4):
            if profile_matrix[j][i] > max_num:
                max_num = profile_matrix[j][i]
                max_row = j

        common_seq += bases[max_row]

    # Print the profile matrix
    print('A:', *profile_matrix[0])
    print('C:', *profile_matrix[1])
    print('G:', *profile_matrix[2])
    print('T:', *profile_matrix[3])

    return common_seq


if __name__ == '__main__':
    filename = input('Enter a file path: ')
    print(most_likely_common_ancestor(filename))

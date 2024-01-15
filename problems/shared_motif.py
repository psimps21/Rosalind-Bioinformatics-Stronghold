"""
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

from fasta_parser import FASTA
import numpy


def lcss(filename):
    seqs, _ = FASTA(filename)
    seqs = [str(s) for s in seqs.values()]
    first = seqs[0]
    len_first = len(first)

    lcs = ''

    for i in range(len_first):
        for j in range(i+1, len_first+1):
            shared = True
            sbstr = first[i:j]

            for k in range(1, len(seqs)):
                if sbstr not in seqs[k]:
                    shared = False
                    break

            if shared and len(sbstr) > len(lcs):
                lcs = sbstr

    return lcs


############### dynamic programming solution attempt ############

def longest_substring(filename):
    seqs, _ = FASTA(filename)
    seqs = [' '+ seq for seq in seqs.values()]
    dims = [len(seq) for seq in seqs]
    matrix = numpy.zeros(tuple(dims), dtype=int)

    inx = [0] * len(dims)

    # A tuple containing the current max length common substring, and tuple of its position in the matrix
    max_len = 0
    max_inx = inx
    final_matrix, max_len, max_inx = fill_matrix(matrix, dims, seqs, inx, max_len, max_inx)
    # print(max_len, max_inx)

    start, end = max_inx[0] - max_len + 1, max_inx[0] + 1
    # print(start, end, seqs[0][7])
    lcs = seqs[0][start:end]

    return lcs


def fill_matrix(matrix, dims, seqs, inx, max_len, max_inx):
    if len(dims) == 0:
        if evalu(inx, seqs):
            inx = tuple(inx)
            prev = tuple([i-1 for i in inx])
            new_value = 1
            if matrix[prev] != 0:
                new_value = matrix[prev] + 1

            matrix[inx] = new_value

            if new_value >= max_len:
                max_len, max_inx = (new_value, inx)

        return matrix, max_len, max_inx

    else:
        new_dims = dims[1:]
        for x in range(dims[0]):
            current_dim = matrix.ndim - len(dims)
            inx[current_dim] = x
            matrix, max_len, max_inx= fill_matrix(matrix, new_dims, seqs, inx, max_len, max_inx)

    return matrix, max_len, max_inx


# Return a boolean representing whether the bases at a given matrix index match
def evalu(inx, seqs):
    inx = tuple(inx)
    for i in range(len(inx)):
        if seqs[i][inx[i]] != seqs[-1][inx[-1]]:
            return False

    if seqs[-1][inx[-1]] == ' ':
        return False

    return True


if __name__=='__main__':
    filename = input('Enter a file path: ')
    print(lcss(filename))

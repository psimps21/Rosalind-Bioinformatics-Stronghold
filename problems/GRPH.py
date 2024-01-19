"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as fasta:
        sequence_map = {}

        for line in fasta.readlines():
            if line.startswith('>'):
                name = line[1:].strip('\n')
                sequence_map[name] = ''

            else:
                sequence_map[name] += line.strip('\n')

    return sequence_map

def overlap_seqs(seq_map, lim):
    pair_set = set()
    for k1, v1 in seq_map.items():
        for k2, v2 in seq_map.items():
            if v1[-lim:] == v2[:lim] and v1 != v2:
                pair_set.add((k1, k2))

    return  pair_set


if __name__ =='__main__':
    input_f = sys.argv[1]
    seq_map = ReadInput(input_f)

    pairs = overlap_seqs(seq_map, 3)
    [print(*i) for i in pairs]

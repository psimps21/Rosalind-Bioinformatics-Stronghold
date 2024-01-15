"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

def overlap_seqs(filename, lim):
    with open(filename, 'r') as file:
        seq_dict = {}
        seq = ''

        for line in file:
            line = line.replace('\n', '')
            if line[0] == '>':
                if not seq:
                    read_name = line[1:]
                    continue

                seq_dict[read_name] = seq
                seq = ''
                read_name = line[1:]
                continue

            seq += line

    seq_dict[read_name] = seq

    pair_set = set()
    for k1, v1 in seq_dict.items():
        for k2, v2 in seq_dict.items():
            if v1[-lim:] == v2[:lim] and v1 != v2:
                pair_set.add((k1, k2))

    return  pair_set


if __name__ =='__main__':
    filename = input('Enter a file path: ')
    pairs = overlap_seqs(filename, 3)
    [print(*i) for i in pairs]

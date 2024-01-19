"""
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
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
    
    return sequence_list

def lcss(seq_list):
    seq_list = sorted(seq_list, key=lambda x: len(x))

    shortest_seq = seq_list[0]
    lcs_len = len(shortest_seq)
    lcs = ''
    # For each possoble substring length (descending)
    while lcs_len > 0:
        lcs_start = 0
        # For each possible substring start position
        while len(lcs) == 0 and lcs_start <= len(shortest_seq) - lcs_len:
            substr = shortest_seq[lcs_start:lcs_start+lcs_len]

            seq_idx = 1
            while seq_idx < len(seq_list) and substr in seq_list[seq_idx]:
                seq_idx += 1

            if seq_idx == len(seq_list):
                lcs = substr

            lcs_start += 1
        lcs_len -= 1
    
    return lcs


if __name__=='__main__':
    input_f = sys.argv[1]
    seq_list = ReadInput(input_f)

    print('LCS:',lcss(seq_list))
    

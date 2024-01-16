"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    return data[0], data[1]

def sliding_window(seq, motif):
    motif_loc_list = []
    for idx in range(len(seq)-len(motif)+1):
        if seq[idx:idx+len(motif)] == motif:
            motif_loc_list.append(idx+1) # ind+1 for 1 based indexing

    return  motif_loc_list

if __name__ == '__main__':
    input_f = sys.argv[1]
    seq, motif= ReadInput(input_f)

    motif_list = sliding_window(seq, motif)
    print(*motif_list)
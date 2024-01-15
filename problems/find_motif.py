"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

def motif_loc(seq, motif):
    motif_loc_list = []
    for ind, char in enumerate(seq):
        if char == motif[0] and ind <= len(seq)-len(motif):
            if seq[ind:ind+len(motif)] == motif:
                motif_loc_list.append(ind) # ind+1 for 1 based indexing

    return  motif_loc_list


if __name__ == '__main__':
    sequence = input('Enter a DNA sequence: ')
    mtf = input('Enter a motif: ')
    motif_list = motif_loc(sequence, mtf)
    print(*motif_list)
"""
Given: A collection of at most 5 pairs of permutations, all of which have length 10.

Return: The reversal distance between each permutation pair.
"""
import sys
import numpy as np

def ReadInput(input):
    with open(input, 'r') as f:
        lines = f.readlines()
    
    seq_pairs = []
    for i in range(0,len(lines),3):
        seq1 = np.array([int(x) for x in lines[i].strip().split()])
        seq2 = np.array([int(x) for x in lines[i+1].strip().split()])
        seq_pairs.append((seq1, seq2))

    return seq_pairs

# Computes the length of the prefix and suffix match for seq1 and seq2
def ComputeEndMatches(seq1, seq2):
    b_match, e_match = 0,0
    i,j = 0,1

    # Find length of beginning match
    while i < len(seq1) and seq1[i] == seq2[i]:
        b_match += 1
        i += 1

    # Find length of ending matvh match
    while j <= len(seq1) and seq1[-j] == seq2[-j]:
        e_match += 1
        j += 1

    return b_match, e_match

# Performs a reversal correct the first unmatched index in seq2
def ReverseOneInterval(seq1, seq2, b_match, e_match):
    # idx = np.arange(len(seq1))
    # swap_idx = seq1.index[seq1 == seq2[b_match]] + 1

    swap_idx = np.where(seq1 == seq2[b_match])[0].item() + 1
    # print('swap_idx, swap_val:', swap_idx, seq1[swap_idx-1])

    new_seq1 = np.concatenate((seq1[:b_match], seq1[b_match: swap_idx][::-1], seq1[swap_idx:]))
    # print('Old seq1:', seq1)
    # print('Old seq2:', seq2)
    # print('New seq1:', new_seq1)

    b_match, e_match = ComputeEndMatches(new_seq1,seq2)

    # print('post function New seq1:', new_seq1)

    return new_seq1, b_match, e_match

def ReversalDistance(seq1, seq2):

    if np.array_equal(seq1,seq2):
        return 0

    rev_dist = 0
    b_match, e_match = ComputeEndMatches(seq1,seq2)
    while b_match != len(seq1):
        rev_dist += 1
        seq1, b_match, e_match = ReverseOneInterval(seq1, seq2, b_match, e_match)

        # print('Current # reversals:', rev_dist)
        # print(seq1)
        # print(seq2)
        # print()

        if rev_dist == 11:
            break

    return rev_dist
    
# Perform a reversal of the seqeince at the given indexes (inclusive)
def PerformeReversal(seq, inx1,inx2):
    new_seq = np.concatenate((seq[:inx1], seq[inx1: inx2+1][::-1], seq[inx2+1:]))
    return new_seq

# Return a list with the indices of all breakpoints in the permutation
def FindBreakpoints(seq, target):
    # Append end toke to 

    # Populate dictionary with next number in the seq for each target value
    target_dict = dict()
    for inx, v in enumerate(target):
        if inx == len(target) - 1:
            target_dict[v] = target[inx+1]
        else:
            target_dict[v] = 11

    # Find the index of all breakpoints
    bp_list = []

    # Check initial break point
    if seq[0] == target[0]:
        bp_list.append(0)
    
    for inx, v in enumerate(seq):
        if inx == len(seq) - 1:
            if v == target[inx]:
                bp_list.append(inx+1)
        else:
            target_post = target_dict[v]
            if seq[inx+1] == target_post:
                bp_list.append(inx+1)

    return bp_list

# return new seq1 after performing the greedily chosen reversal
def GreedyReversalChoice(seq1,seq2):
    bp_list = FindBreakpoints(seq1, seq2)

    if bp_list == 2:
        pass
    
    for i in range(1, len(bp_list)):
        for j in range(i, len(bp_list)):
            pass

if __name__ == '__main__':
    # Input file path
    input = sys.argv[1]

    seq_pairs = ReadInput(input)
    # print(*seq_pairs,sep='\n')

    # print(ReversalDistance(seq_pairs[0][0],seq_pairs[0][1]))

    rev_dists = [ReversalDistance(a,b) for a,b in seq_pairs]
    print(*rev_dists)

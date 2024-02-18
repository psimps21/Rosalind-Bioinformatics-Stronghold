"""
Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""
import sys

def ReadFromFile(input_f):
    with open(input_f, 'r') as f:
        data = f.readlines()

    # seq = np.array([int(x) for x in data[-1].strip().split()])
    seq = [int(x) for x in data[-1].strip().split()]

    return seq


def LIS(seq_arr):
    lis_seqs = [[] for _ in range(len(seq_arr))]
    lis_seqs[0].append(seq_arr[0])

    for i in range(1,len(seq_arr)):
        for j in range(i):
            if seq_arr[j] < seq_arr[i] and (len(lis_seqs[i]) < len(lis_seqs[j]) + 1):
                lis_seqs[i] = lis_seqs[j].copy()
        
        lis_seqs[i].append(seq_arr[i])

    lis = []
    for x in lis_seqs:
        if len(x) > len(lis):
            lis = x

    return lis


if __name__ == '__main__':
    input_f = sys.argv[1]

    seq_arr = ReadFromFile(input_f)
    rev_seq_arr = -1 * seq_arr

    lis = LIS(seq_arr)
    lds = [-1*x for x in LIS(-1 * seq_arr)]

    # lis = constructPrintLIS(seq_arr, len(seq_arr))
    # lds = [-1*x for x in constructPrintLIS(rev_seq_arr, len(rev_seq_arr))]

    print(f'The LIS is:',*lis)
    print(f'The LDS is:',*lds)

# 5 4 1 2 3
# 5 4 1 2 3


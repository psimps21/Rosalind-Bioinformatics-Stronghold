"""
Given: A permutation of at most 12 symbols defining an ordered alphabet A
 and a positive integer n ( n ≤ 4 ).

Return: All strings of length at most n
 formed from A, ordered lexicographically. 
 (Note: As in “Enumerating k-mers Lexicographically”, alphabet order
  is based on the order in which the symbols are given.)
"""

import itertools as it
import sys

def ReadFromFile(input_f):
    with open(input_f, 'r') as f:
        data = f.readlines()

    alphabet = [x for x in data[0].strip().split()]
    n = int(data[-1].strip())

    return alphabet, n

        
def OrderedStrings(alphabet, n):
    seqs = alphabet.copy()

    for i in range(2,n+1):
        seqs += [''.join(c) for c in it.product(''.join(alphabet), repeat=i)]

    sorted_seqs = sorted(seqs,key=lambda word: [''.join(alphabet).index(c) for c in word])

    return sorted_seqs


if __name__ == '__main__':
    input_f = sys.argv[1]

    alphabet, n = ReadFromFile(input_f)

    sorted_seqs = OrderedStrings(alphabet, n)

    with open('saved/saved_lexv.txt','w') as f:
        f.writelines([x+'\n' for x in sorted_seqs])




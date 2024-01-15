"""
Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically
(use the standard order of symbols in the English alphabet).
"""
from itertools import product

def k_kmers(filename):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            line = line.replace('\n', '')
            data.append(line)

    alphabet = list(data[0].split(' '))
    k = int(data[1])

    for p in product(alphabet, repeat=k):
        print(''.join(p))

############## Recurssive Solution ####################

def lexico_kmers(filename):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            line = line.replace('\n', '')
            data.append(line)

    alphabet = list(data[0].split(' '))
    k = int(data[1])

    kmers = make_kmers(alphabet, [], [0]*k, 0, k)

    return kmers


def make_kmers(alphabet, kmers, indicies, lvl, k):
    if lvl == k:
        kmer = ''
        for i in range(k):
            kmer += alphabet[indicies[i]]

        print(kmer)
        kmers.append(kmer)

        return kmers

    else:
        for i in  range(len(alphabet)):
            indicies[lvl] = i
            kmers = make_kmers(alphabet, kmers, indicies, lvl+1, k)

        return kmers


if __name__ == '__main__':
    filename = input('Entera file path: ')
    kmers = lexico_kmers(filename)
    # k_kmers(filename)


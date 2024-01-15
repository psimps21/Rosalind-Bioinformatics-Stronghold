"""
Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
"""
from fasta_parser import FASTA

def number_to_pattern(inx, k):
    symbols = {
        0: 'A',
        1: 'C',
        2: 'G',
        3: 'T'
    }

    prefix = inx // 4
    end = inx % 4

    if k == 1:
        return symbols[end]

    return number_to_pattern(prefix, k-1) + symbols[end]

def pattern_to_number(pattrn):
    bases = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }

    if len(pattrn) == 1:
        return bases[pattrn]

    prefix = pattrn[:-1]
    end = pattrn[-1]

    return 4 * pattern_to_number(prefix) + bases[end]

def kmer_comp(filename):
    seq, _ = FASTA(filename)
    seq = [str(s) for s in seq.values()]
    array = [0] * 4**4
    k = 4

    for i in range(0, len(seq[0])-k+1):
        array[pattern_to_number(seq[0][i:i+k])] += 1

    return array

if __name__ == '__main__':
    filename = input('Enter a file path: ')
    arr = kmer_comp(filename)
    print(*arr)
    # print(number_to_pattern(2, 4))
    # print(pattern_to_number('AAAG'))
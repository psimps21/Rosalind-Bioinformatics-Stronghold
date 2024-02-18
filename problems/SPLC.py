"""
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are
given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s.
(Note: Only one solution will exist for the dataset provided.)
"""
import sys
import re

def ReadInput(input_f):
    with open(input_f, 'r') as fasta:
        sequence_list = []

        for line in fasta.readlines():
            if line.startswith('>'):
                sequence_list.append('')

            else:
                sequence_list[-1] += line.strip('\n')
    
    return sequence_list[0], sequence_list[1:]

def dnaToProtein(dna):
    # Code for codon table found at http://www.petercollingridge.co.uk/tutorials/bioinformatics/codon-table/
    bases = "TCAG"
    codons = [a + b + c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))

    aa_seq = ''
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if codon_table[codon] == '*':
            break
        aa_seq += codon_table[codon]

    return aa_seq

def splicing(seq, introns):
    for i in introns:
        seq = re.sub(i,'',seq)

    return dnaToProtein(seq)


if __name__ == '__main__':
    input_f = sys.argv[1]
    seq, introns = ReadInput(input_f)
    print()
    print(splicing(seq, introns))
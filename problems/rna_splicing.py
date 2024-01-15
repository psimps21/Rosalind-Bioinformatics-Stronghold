"""
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are
given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s.
(Note: Only one solution will exist for the dataset provided.)
"""
from fasta_parser import FASTA

bases = "tcag"
codons = [a + b + c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

def translate(seq):
    seq = seq.lower().replace('\n', '').replace(' ', '')
    peptide = ''

    for i in range(0, len(seq), 3):
        codon = seq[i: i + 3]
        amino_acid = codon_table.get(codon, '*')
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break

    return peptide

def splicing(filename):
    seqs, _ = FASTA(filename)
    seqs = [str(s) for s in seqs.values()]
    seq = seqs[0]
    introns = seqs[1:]

    for i in introns:
        for j in range(0, len(seq)-len(i)+1):
            if seq[j:j+len(i)] == i:
                seq = seq[:j] + seq[j+len(i):]
                break

    return translate(seq)


if __name__ == '__main__':
    filename = input('Enter a file path: ')
    print(splicing(filename))
"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000.
(Don't neglect the importance of the stop codon in protein translation.)
"""


def posibble_mrnas(aa_seq):
    aa_codon_dict = {
         'A': ['GCU', 'GCC', 'GCA', 'GCG'],
         'C': ['UGU', 'UGC'],
         'D': ['GAU', 'GAC'],
         'E': ['GAA', 'GAG'],
         'F': ['UUU', 'UUC'],
         'G': ['GGU', 'GGC', 'GGA', 'GGG'],
         'H': ['CAU', 'CAC'],
         'I': ['AUU', 'AUC', 'AUA'],
         'K': ['AAA', 'AAG'],
         'L': ['CUU', 'CUC', 'UUA', 'CUA', 'UUG', 'CUG'],
         'M': ['AUG'],
         'N': ['AAU', 'AAC'],
         'P': ['CCU', 'CCC', 'CCA', 'CCG'],
         'Q': ['CAA', 'CAG'],
         'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'],
         'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
         'Stop': ['UAA', 'UAG', 'UGA'],
         'T': ['ACU', 'ACC', 'ACA', 'ACG'],
         'V': ['GUU', 'GUC', 'GUA', 'GUG'],
         'W': ['UGG'],
         'Y': ['UAU', 'UAC']}

    mod = 1
    for aa in aa_seq:
        mod *= len(aa_codon_dict[aa])

    return mod * 3 % 1000000


if __name__ == '__main__':
    prot = input('Enter a protein sequence: ')
    print(posibble_mrnas(prot))


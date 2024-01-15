"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""

def rna_to_protein(rna):
    # Code for codon table found at http://www.petercollingridge.co.uk/tutorials/bioinformatics/codon-table/
    bases = "UCAG"
    codons = [a + b + c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))

    aa_seq = ''
    end = len(rna) % 3
    for i in range(0, len(rna)-end, 3):
        if codon_table[rna[i:i + 3]] == '*':
            break

        aa_seq += codon_table[rna[i:i+3]]

    return aa_seq


if __name__ == '__main__':
    rna = input('Enter an RNA sequence: ')
    print(rna_to_protein(rna))

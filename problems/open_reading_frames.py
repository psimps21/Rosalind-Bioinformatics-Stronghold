"""
Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any
order.
"""

from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bioinformatics_Stronghold.problems.RNA import insertU
from Bioinformatics_Stronghold.problems.REVC import reverse_comp

def rna_to_protein(rna):
    # Code found at http://www.petercollingridge.co.uk/tutorials/bioinformatics/codon-table/
    bases = "UCAG"
    codons = [a + b + c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    codon_table = dict(zip(codons, amino_acids))

    aa_seq = ''
    end = len(rna) % 3
    for i in range(0, len(rna)-end, 3):
        aa_seq += codon_table[rna[i:i+3]]

    return aa_seq

def orf_seqs(filename):
    with open(filename) as fasta:
        # Retrieve sequence from fasta
        for chrm, seq in SimpleFastaParser(fasta):
            dna = seq

    # Get the forward and backwards rna strands
    rna = insertU(dna)
    rev_rna = insertU(reverse_comp(dna))

    prot_seqs = []

    # Loop through open reading frames
    for orf in range(3):
        frwd_res = rna_to_protein(rna[orf:])
        rev_res = rna_to_protein(rev_rna[orf:])

        # For forward and reverse seqs
        for res in [frwd_res, rev_res]:
            running_seq = False
            r_seqs = []

            # Enumerate amino acid residue
            for inx, aa in enumerate(res):
                if running_seq:
                    if aa == "*":
                        running_seq = False
                        for pair in r_seqs:
                            if pair[1] is None:
                                pair[1] = inx

                    elif aa == 'M':
                        r_seqs.append([inx, None])

                else:
                    if aa == 'M':
                        running_seq = True
                        r_seqs.append([inx, None])

            # Add complete residues to final list
            for start, end in r_seqs:
                if end is not None:
                    prot = res[start:end]
                    prot_seqs.append(prot)

    return set(prot_seqs)


if __name__ == "__main__":
    filename = input('Enter a file path: ')
    p_seqs = orf_seqs(filename)
    print(*p_seqs, sep='\n')

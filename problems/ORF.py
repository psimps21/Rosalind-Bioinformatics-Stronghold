"""
Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any
order.
"""
import sys, re

def ReadInput(input_f):
    with open(input_f, 'r') as fasta:
        sequence_list = []

        for line in fasta.readlines():
            if line.startswith('>'):
                sequence_list.append('')

            else:
                sequence_list[-1] += line.strip('\n')
    
    return sequence_list[-1]

def rev_comp(s):
    return s[::-1].translate(str.maketrans('ACGT', 'TGCA'))

def insertU(dna):
    return dna.replace('T', 'U')

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

def orf_seqs(dna):
    # Get the forward and backwards rna strands
    rna = insertU(dna)
    rev_rna = insertU(rev_comp(dna))

    prot_seqs = []

    # regex pattern
    pattern = r'(?=(M[A-Z]*\*))'
    
    for i in range(3):
        fwd_aa = rna_to_protein(rna[i:])
        rev_aa = rna_to_protein(rev_rna[i:])

        fwd_res = re.findall(pattern, fwd_aa)
        rev_res = re.findall(pattern, rev_aa)

        prot_seqs += [x[:-1] for x in fwd_res] + [x[:-1] for x in rev_res]

    return set(prot_seqs)

# def orf_seqs(dna):
#     # Get the forward and backwards rna strands
#     rna = insertU(dna)
#     rev_rna = insertU(rev_comp(dna))

#     prot_seqs = []

#     # Loop through open reading frames
#     for orf in range(3):
#         frwd_res = rna_to_protein(rna[orf:])
#         rev_res = rna_to_protein(rev_rna[orf:])

#         # For forward and reverse seqs
#         for res in [frwd_res, rev_res]:
#             running_seq = False
#             r_seqs = []

#             # Enumerate amino acid residue
#             for inx, aa in enumerate(res):
#                 if running_seq:
#                     if aa == "*":
#                         running_seq = False
#                         for pair in r_seqs:
#                             if pair[1] is None:
#                                 pair[1] = inx

#                     elif aa == 'M':
#                         r_seqs.append([inx, None])

#                 else:
#                     if aa == 'M':
#                         running_seq = True
#                         r_seqs.append([inx, None])

#             # Add complete residues to final list
#             for start, end in r_seqs:
#                 if end is not None:
#                     prot = res[start:end]
#                     prot_seqs.append(prot)

#     return set(prot_seqs)

if __name__ == "__main__":
    input_f = sys.argv[1]
    dna = ReadInput(input_f)

    p_seqs = orf_seqs(dna)
    print(*p_seqs, sep='\n')

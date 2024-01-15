from Bioinformatics_Stronghold.problems.REVC import reverse_comp
from Bio import SeqIO

def rev_pal(seq):
    pals = {}
    for i in range(4,13):
        for j in (0,len(seq)):
            if seq[j:j+i] == reverse_comp(seq[j:j+i]):
                print(seq[j:j + i])
                print(reverse_comp(seq[j:j + i]))
                pals[j] = i

    for k, v in pals.items():
        print(k, v)


if __name__ == '__main__':
    rev_pal('TCAATGCATGCGGGTCTATATGCAT')


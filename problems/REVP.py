import sys

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

def rev_pal(seq):
    rc_seq = rev_comp(seq)[::-1]

    pals = {}
    for i in range(4,13):
        for j in range(0,len(seq)-i+1):
            if seq[j:j+i] == rev_comp(seq[j:j+i]):
                pals[j+1] = i

    for k, v in pals.items():
        print(k, v)

if __name__ == '__main__':
    input_f = sys.argv[1]
    dna = ReadInput(input_f)
    # print(dna)

    rev_pal(dna)


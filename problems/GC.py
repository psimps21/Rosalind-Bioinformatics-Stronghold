"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows
for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as fasta:
        sequence_map = {}

        for line in fasta.readlines():
            if line.startswith('>'):
                name = line[1:].strip('\n')
                sequence_map[name] = ''

            else:
                sequence_map[name] += line.strip('\n')

    return sequence_map

def GCContent(seq):
    gc_count = 0
    for nt in seq:
        if nt == 'G' or nt == 'C':
            gc_count += 1
    
    return round(gc_count / len(seq) * 100, 6)

def BestGCContent(sequence_map):
    best_gc = (None, 0)
    for name, seq in sequence_map.items():
        gc = GCContent(seq)

        if gc > best_gc[1]:
            best_gc = (name, gc)
    
    return best_gc


if __name__ == '__main__':
    input_f = sys.argv[1]
    seq_map = ReadInput(input_f)

    name, gc = BestGCContent(seq_map)
    print(f'{name}\n{gc}')









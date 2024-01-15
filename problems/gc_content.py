"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows
for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below
"""

def gccontent(filename):
    with open(filename, "r") as file:
        strand_dict = {}
        seq_count = 0
        gc_count = 0
        running_seq = False
        strand_id = ''
        for line in file:
            line = line.replace('\n', '')
            if line[0] == ">":
                if not running_seq:
                    strand_id += line[1:]
                    running_seq = True
                    continue

                strand_dict[strand_id] = gc_count/seq_count*100
                seq_count = 0
                gc_count = 0
                strand_id = line[1:]
                continue

            for char in line:
                seq_count += 1
                if char == 'G' or char == 'C':

                    gc_count += 1

    strand_dict[strand_id] = gc_count / seq_count*100

    best_id = strand_id
    best_cg = strand_dict[strand_id]
    for k, v in strand_dict.items():
        if v > best_cg:
            best_cg = v
            best_id = k

    return best_id, best_cg


if __name__ == '__main__':
    filename = input('Enter a file path: ')
    name, value = gccontent(filename)
    print(name, value)









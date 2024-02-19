"""
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as fasta:
        sequence_list = []

        for line in fasta.readlines():
            if line.startswith('>'):
                sequence_list.append('')

            else:
                sequence_list[-1] += line.strip('\n')
    
    return sequence_list[0], sequence_list[1]

def tt_ratio(s,t):
    itions = {'A': 'G',
              'G': 'A',
              'C': 'T',
              'T': 'C'}

    t1, t2 = 0, 0 # transition, transversion

    for i in range(len(s[0])):
        if s[0][i] != t[1][i]:
            if s[0][i] == itions[t[1][i]]:
                t1 += 1
            else:
                t2 += 1

    return t1/t2


if __name__ == '__main__':
    input_f = sys.argv[1]
    s, t = ReadInput(input_f)
    print(tt_ratio(s,t))

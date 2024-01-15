"""
Given: A collection of n
 ( n ≤ 10 ) DNA strings s1,…,sn of equal length (at most 1 kbp). 
 Strings are given in FASTA format.

Return: The matrix D
 corresponding to the p-distance d_p on the given strings. As always,
 note that your answer is allowed an absolute error of 0.001.
"""
import numpy as np
import sys
from Bio import SeqIO


def ReadFromFile(input_f):
    seqs = []
    with open(input_f, 'r') as f:
        for record in SeqIO.parse(f, 'fasta'):
            seqs.append(str(record.seq))

    return seqs

def HammingDistance(str1, str2):
    dis = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            dis += 1
    
    return dis

def DistanceMatrix(seqs):
    n = len(seqs)
    dis_mtx = np.zeros((n,n))

    for i in range(n):
        for j in range(i):
            dis = HammingDistance(seqs[i],seqs[j])
            dis_mtx[i,j] = dis
            dis_mtx[j,i] = dis

    return dis_mtx / len(seqs[0])


if __name__ == '__main__':
    input_f = sys.argv[1]

    seqs = ReadFromFile(input_f)

    dis_mtx = DistanceMatrix(seqs)

    save_f = 'saved/saved_pdst.txt'
    np.savetxt(save_f,dis_mtx, fmt='%.05f')
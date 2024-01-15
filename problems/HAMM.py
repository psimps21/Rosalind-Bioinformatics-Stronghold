"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp)

Return: The Hamming distance dH(s,t)
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    return data[0], data[1]

def count_pm(s, t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    return count

if __name__ == '__main__':
    input_f = sys.argv[1]
    s, t = ReadInput(input_f)\

    print(count_pm(s, t))

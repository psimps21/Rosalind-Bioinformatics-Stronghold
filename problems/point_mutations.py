"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp)

Return: The Hamming distance dH(s,t)
"""

def count_pm(s, t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    return count

if __name__ == '__main__':
    m = input('Enter a sequence: ')
    n = input('Enter a sequence: ')
    print(count_pm(m, n))

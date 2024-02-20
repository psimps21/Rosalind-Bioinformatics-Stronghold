"""
Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A∪B, A−B, A∩B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).
"""
import sys

def ReadFile(input_f):
    with open(input_f, 'r') as f:
        data = [x.strip() for x in f.readlines()]
    
    n = int(data[0])
    a = set([int(x) for x in data[1][1:-1].split(', ')])
    b = set([int(x) for x in data[2][1:-1].split(', ')])

    return n, a, b

def sets(n, a, b):
    u = set(range(1, n+1))

    union = a.union(b)
    intsct = a.intersection(b)
    a_diff_b = a.difference(b)
    b_diff_a = b.difference(a)
    comp_a = u.difference(a)
    comp_b = u.difference(b)

    sets = [union, intsct, a_diff_b, b_diff_a, comp_a, comp_b]

    with open('saved/seto.txt', 'w') as f:
        for s in sets:
            f.write('{' + ", ".join([str(x) for x in s]) + '}\n')

    # for s in sets:
    #     print(s)
        # print(f'{{{", ".join(s)}}}')

    # return union, intsct, a_diff_b, b_diff_a, comp_a, comp_b

if __name__ == '__main__':
    input_f = sys.argv[1]
    n, a, b = ReadFile(input_f)

    sets(n, a, b)
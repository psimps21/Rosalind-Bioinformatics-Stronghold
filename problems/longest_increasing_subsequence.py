"""
Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""
def LIS(a,n):
    lis = [1] * n
    # lis_inx = [n-1]
    best = []
    lis_map = {inx:[v] for inx,v in enumerate(a)}
    for i in range(n-2,-1,-1):
        max_inx = i
        for j in range(n-1,i,-1):
            if a[i] < a[j]:
                if max_inx == i:
                    max_inx = j
                elif 1+lis[j] > 1+lis[max_inx]:
                    max_inx = j
        
        print(a[i],i,max_inx)
        if max_inx != i:
            # lis_map[i] += lis_map[max_inx]
            if 1 + lis[max_inx] > lis[i+1]:
                lis[i] = 1 + lis[max_inx]
                # best = lis_map[i]
        else:
            lis[i] = lis[i+1]
            
            
            # if lis_inx[-1] != max_inx:
            #     lis_inx[-1] = max_inx
            # lis_inx += [i]
        # else:
        #     lis[i] = lis[i+1]
    # print('max lis',max(lis))
    print(lis)
    # print(best)
    # print(lis_inx)
    
    return ' '.join([str(x) for x in best])

def LDS(a,n):
    from pprint import pprint
    lis = [1] * n
    lis_map = {inx:[v] for inx,v in enumerate(a)}
    # lis_inx = [n-1]
    for i in range(n-2,-1,-1):
        max_inx = i
        for j in range(n-1,i,-1):
            if a[i] < a[j]:
                if max_inx == i:
                    max_inx = j
                elif 1+lis[j] >= 1+lis[max_inx]:
                    max_inx = j
        
        if max_inx != i:
            lis[i] = 1 + lis[max_inx]
            lis_map[i] += lis_map[max_inx]
            best = lis_map[i]
        else:
            lis[i] = lis[i+1]
    # print(lis)
    # pprint(lis_map)
    # print(lis_inx)
    
    return ' '.join([str(x) for x in best[::-1]])

def reader(path):
    with open(path,'r') as f:
        n, a_str = f.readlines()
    
    return int(n), a_str.strip()


if __name__ == '__main__':
    n = 5 # int(input('Enter n: '))
    # a_str = '5 1 4 2 3'#[::-1] # input('Enter permutation: ')
    a_str = "0 4 2 20 21 22 3 5 6 7"
    # a_str = "0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15"
    # n, a_str = reader('/Users/parkersimpson/Downloads/rosalind_lgis (1).txt')
    a = [int(x) for x in a_str.split()]
    b = a[::-1]
    # print(LongestIncreasingSubsequence(a,n))
    print(*a)
    print(*b)
    print()
    # print(len(a))
    print(LDS(a,len(a)))
    print()
    print(LDS(b,len(b)))




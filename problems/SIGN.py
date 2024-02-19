""""
Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations
(you may list the signed permutations in any order).
"""
import math

def enum_orderings(lst):
    if len(lst) == 2:
        return [[p] for p in lst]

    perm_list = []
    half = len(lst)//2
    for i in range(half):
        p_new_first = lst[i]
        n_new_first = -p_new_first

        leftover = lst[:i] + lst[i+1:half+i] + lst[half+i+1:]
        for p in enum_orderings(leftover):
            perm_list.append([p_new_first] + p)
            perm_list.append([n_new_first] + p)

    return perm_list

def enum_caller(n):
    lst = [*range(1,n+1)] + [*range(-1,-(n+1),-1)]
    perm_list = enum_orderings(lst)

    return perm_list, len(perm_list)


if __name__ == '__main__':
    n = 3
    perms, num = enum_caller(n)
    print(num)
    [print(*p) for p in perms]
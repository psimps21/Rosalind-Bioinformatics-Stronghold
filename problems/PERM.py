"""
Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    return int(data[0])

def perms(lst):
    if len(lst) == 1:
        return [lst]

    perm_list = []
    for i in range(len(lst)):
        new_first = lst[i]

        leftover = lst[:i] + lst[i+1:]
        for p in perms(leftover):
            perm_list.append([new_first] + p)

    return perm_list


def find_perms(n):
    lst = [*range(1,n+1)]
    perm_list = perms(lst)

    return perm_list


if __name__ == '__main__':
    # input_f = sys.argv[1]
    # num = ReadInput(input_f)
    num = 4

    perms_list = find_perms(num)

    print(len(perms_list))
    [print(*p) for p in perms_list]

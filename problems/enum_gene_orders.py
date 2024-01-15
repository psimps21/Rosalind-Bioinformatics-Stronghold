"""
Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""

def perms(lst):
    if len(lst) == 0:
        return []

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

    return perm_list, len(perm_list)


if __name__ == '__main__':
    # n = input('Enter a value for n: ')
    n=3
    perms, nums = find_perms(n)
    print(nums)
    [print(*p) for p in perms]
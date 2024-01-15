from math import factorial

def hetorz_prob(k, n):
    total = 0
    for i in range(0, n):
        gen_num = 2**k
        comb = factorial(gen_num)/(factorial(gen_num-i)*factorial(i))
        total += comb * (.75**(gen_num-i)) * (.25**i)

    return round(1 - total, 3)


if __name__ == '__main__':
    k = int(input("Enter a value for k: "))
    n = int(input('Enter a value for n: '))
    print(hetorz_prob(k, n))

"""
Given: Three positive integers k,m, n representing a population containing k+m+n organisms:
                                                                    k individuals are homozygous dominant for a factor,
                                                                    m are heterozygous,
                                                                    and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

def dominant_offsring(k, m ,n):
    '''
    The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
    Assuming that any two organisms can mate
    :param k: Number of homozygous dominant organisms
    :param m: Number of heterozygous organisms
    :param n: Number of homozygous recessive individuals
    :return: The probability that two randomly selected mating organisms will produce an individual possessing a
    dominant allele
    '''
    pop = k + m + n
    pop2 = k + m + n - 1

    rec_prob = ((m/pop) * (n/pop2) * .5)*2 + ((n/pop) * ((n-1)/pop2)) + ((m/pop) * ((m-1)/pop2) * .25)

    return 1 - rec_prob

if __name__ == "__main__":
    k = input('Enter a value for k: ')
    m = input('Enter a value for m: ')
    n = input('Enter a value for n: ')
    print(dominant_offsring(k, m, n))

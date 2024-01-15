"""
Given: Three positive integers k,m, n representing a population containing k+m+n organisms:
            k individuals are homozygous dominant for a factor,
            m are heterozygous,
            and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        data = f.readlines()
    
    k, m, n = [int(x) for x in data[0].strip().split()]

    return k, m, n

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

    # Prob of rec off soring from: (ht, rec), (rec, het), (het,het), (rec,rec)
    rec_prob = ((m/pop) * (n/pop2) * .5)*2 + ((n/pop) * ((n-1)/pop2)) + ((m/pop) * ((m-1)/pop2) * .25)

    return round(1 - rec_prob, 6)

if __name__ == "__main__":
    input_f = sys.argv[1]
    k, m, n = ReadInput(input_f)

    print(dominant_offsring(k, m, n))

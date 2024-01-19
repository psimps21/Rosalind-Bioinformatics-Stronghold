"""
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of
couples in a population possessing each genotype pairing for a given factor. In order, the six given integers
represent the number of couples having the following genotypes: :
                                                                    1. AA-AA
                                                                    2. AA-Aa
                                                                    3. AA-aa
                                                                    4. Aa-Aa
                                                                    5. Aa-aa
                                                                    6. aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the
assumption that every couple has exactly two offspring.
"""
import sys

def ReadInput(input_f):
    with open(input_f, 'r') as f:
        data = f.readlines()
    
    data = [int(x) for x in data[0].strip().split()]

    return data

def offspring(nums):
    # The total number of offspring
    total_offspring = sum(nums) * 2

    # The number of recessive offspring from different parental crosses
    hxh = nums[3] * 1/4 * 2
    hxr = nums[4] * 1/2 * 2
    rxr = nums[5] * 1 * 2

    rec_off = hxh + hxr + rxr

    return total_offspring - rec_off

if __name__ == '__main__':
    input_f = sys.argv[1]
    data = ReadInput(input_f)

    print(offspring(data))

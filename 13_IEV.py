import numpy as np

# pair types:
# 0 - AA-AA
# 1 - AA-Aa
# 2 - AA-aa
# 3 - Aa-Aa
# 4 - Aa-aa
# 5 - aa-aa

def expected_dominant_offspring(genotype_pairs, generation_size):
    """
    Calculates the expected number of offspring having the dominant phenotype.

    genotype_pairs (np.array): gives counts of parent pair types (see above) in current generation
    generation_size (int): number of offspring per pair
    """
    dominant_proportion = np.array([1., 1., 1., 0.75, 0.5, 0.]) # proportion of offspring of pair type i w/ dominant phenotype
    return generation_size * np.dot(genotype_pairs, dominant_proportion)

def test_expected_dominant_offspring(filename):
    with open(filename, 'r') as handle:
        genotype_pairs = np.array([int(x) for x in handle.readline().strip().split()])
    print(expected_dominant_offspring(genotype_pairs, 2)) # problem statement fixes generation_size at 2

test_expected_dominant_offspring("data/rosalind_iev.txt")
from scipy.stats import binom

def proportion_heterozygous(k):
    """
    """
    p = [{"AA": 0.0, "Aa": 1.0, "aa": 0.0}]
    for i in range(1, k+1): # include generation k
        prev = p[i-1]
        p.append({
            "AA": 0.50*prev["AA"] + 0.25*prev["Aa"],
            "Aa": 0.50*prev["AA"] + 0.50*prev["Aa"] + 0.50*prev["aa"],
            "aa":                   0.25*prev["Aa"] + 0.50*prev["aa"]
        })
    return p[k]["Aa"]

def proportion_doubly_heterozygous(k):
    return proportion_heterozygous(k)**2 # independent events, probabilities can be multiplied

def calculate_probability(k, N):
    proportion = proportion_doubly_heterozygous(k)
    num_individuals = 2**k
    return binom.sf(N-1, num_individuals, proportion) # probability of having at least N indidividuals

def test_calculate_probability(filename):
    with open(filename, "r") as handle:
        k, N = [int(x) for x in handle.readline().strip().split()]
    print(calculate_probability(k, N))

test_calculate_probability("data/rosalind_lia.txt")

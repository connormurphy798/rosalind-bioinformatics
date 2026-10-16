import math

def prob_dominant_phenotype(k, m, n):
    N = k + m + n
    rec_rec_pairing = n/N * (n-1)/(N-1)
    rec_het_pairing = 2 * n/N * m/(N-1) * 0.5 # 0.5 reflects probability of a recessive offspring
    het_het_pairing = m/N * (m-1)/(N-1) * 0.25    
    return 1 - (rec_rec_pairing + rec_het_pairing + het_het_pairing)

def test_prob_dominant_phenotype(filename):
    with open(filename, "r") as handle:
        args = [int(x) for x in handle.readline().split()]
    print(prob_dominant_phenotype(*args))

test_prob_dominant_phenotype("data/rosalind_iprb.txt")
def hamming(s, t):
    return sum(a != b for a,b in zip(s,t))

def test_hamming(filename):
    seqs = []
    with open(filename, 'r') as handle:
        for line in handle.readlines():
            seqs.append(line.strip())
    print(hamming(*seqs))

test_hamming("data/rosalind_hamm.txt")

from Bio import SeqIO

def make_consensus_matrix(seqs, nucleotides):
    n = len(seqs[0])
    if not all([len(s) == n for s in seqs]):
        raise ValueError("seqs must all be of the same length")
    matrix = {N: [0 for _ in range(n)] for N in nucleotides}
    for seq in seqs:
        for i, nt in enumerate(seq):
            matrix[nt][i] += 1
    return matrix

def argmax(l):
    return max(range(len(l)), key=lambda x: l[x])

def consensus_sequence(seqs):
    nucleotides = "ACGT"
    matrix = make_consensus_matrix(seqs, nucleotides)
    n = len(seqs[0])
    consensus = [nucleotides[argmax([matrix[N][i] for N in nucleotides])] for i in range(n)]
    return matrix, "".join(consensus)

def test_consensus_sequence(filename):
    seqs = [str(record.seq) for record in SeqIO.parse(filename, "fasta")]
    matrix, consensus = consensus_sequence(seqs)
    print(consensus)
    for N in matrix:
        print(f"{N}:", *matrix[N])

test_consensus_sequence("data/rosalind_cons.txt")
    
from Bio import SeqIO

# NB: the problem doesn't differentiate well between requiring that the sequences not be equal and
# requiring that their labels not be equal. i chose to interpret it as the latter. in other words,
# the sequence labeled Rosalind_0498 won't be compared to itself, but it would be compared to a
# sequence labeled Rosalind_0499 that was of identical sequence content. 

def overlap_graph(seqs, k):
    overlaps = []
    for s in seqs:
        for t in seqs:
            if s != t:                  
                if seqs[s][-k:] == seqs[t][:k]:
                    overlaps.append((s,t))
    return overlaps

def test_overlap_graph(filename):
    seqs = {record.id: str(record.seq) for record in SeqIO.parse(filename, "fasta")}
    overlaps = overlap_graph(seqs, 3) # problem statement fixes k at 3
    for overlap in overlaps:
        print(*overlap)

test_overlap_graph("data/rosalind_grph.txt")
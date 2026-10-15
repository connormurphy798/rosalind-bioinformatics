def reverse_complement(s):
    c = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([c[nt] for nt in s[::-1]])

with open("data/rosalind_revc.txt", "r") as handle:
    print(reverse_complement(handle.readline().strip()))

def count_bases(s):
    counts = {n: 0 for n in "ACGT"}
    for base in s:
        if base in counts:
            counts[base] += 1
    return " ".join([str(v) for v in counts.values()])

def run_test(filename):
    with open(filename, 'r') as handle:
        s = handle.readline()
    return count_bases(s)

print(run_test("data/rosalind_dna.txt"))
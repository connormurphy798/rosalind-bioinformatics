from Bio import SeqIO

def get_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            yield s[i:j]

def longest_common_substring(seqs):
    shortest = min(seqs, key=lambda x: len(x)) # shortest sequence will have the least substrings to check
    lcs = '' # current longest common substring
    for substring in get_substrings(shortest):
        if (len(substring) > len(lcs)) and all(substring in seq for seq in seqs):
            lcs = substring
    return lcs

def test_longest_common_substring(filename):
    seqs = [str(record.seq) for record in SeqIO.parse(filename, "fasta")]
    print(longest_common_substring(seqs))

test_longest_common_substring("data/rosalind_lcsm.txt")
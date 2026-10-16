def substring_indices(s, t):
    indices = []
    m, n = len(s), len(t)
    for i in range(m - n + 1):
        if s[i:i+n] == t:
            indices.append(i+1) # 1-based indexing
    return indices

def test_substring_indices(filename):
    with open(filename, "r") as handle:
        args = [line.strip() for line in handle.readlines()]
    print(*substring_indices(*args))

test_substring_indices("data/rosalind_subs.txt")
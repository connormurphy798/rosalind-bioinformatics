def fib_mortal(n, m):
    totals = [1, 1] 
    for i in range(2, n):
        totals.append(totals[i-1] + totals[i-2])
        if i == m:
            totals[i] -= 1 # founding pair dies
        if i > m:
            totals[i] -= totals[i-m-1]
    return totals[-1]

def test_fib_mortal(filename):
    with open(filename) as handle:
        n, m = [int(x) for x in handle.readline().split()]
    print(fib_mortal(n, m))

test_fib_mortal("data/rosalind_fibd.txt")
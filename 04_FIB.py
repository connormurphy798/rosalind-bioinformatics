def fib(n, k):
    totals = [1, 1]
    for i in range(2, n):
        totals.append(totals[i-1]+k*totals[i-2])
    return totals[-1]

with open("data/rosalind_fib.txt", "r") as handle:
    inputs = [int(x) for x in handle.readline().strip().split()]
    print(fib(*inputs))
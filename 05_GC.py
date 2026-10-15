from Bio import SeqIO

def gc(s):
    count = 0
    for nt in s:
        if nt in "GC":
            count += 1
    return count/len(s)

def gc_fasta(filename):
    d = {}
    for record in SeqIO.parse(filename, "fasta"):
        d[record.id] = gc(str(record.seq))
    m = max(d.items(), key=lambda x: x[1])
    print(m[0])
    print(m[1]*100)

gc_fasta("data/rosalind_gc.txt")

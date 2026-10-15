def transcribe_DNA(t):
    return t.replace("T", "U")

with open("data/rosalind_rna.txt", "r") as handle:
    print(transcribe_DNA(handle.readline()))
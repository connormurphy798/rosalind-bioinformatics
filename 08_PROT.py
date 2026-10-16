def make_genetic_code(filename):
    code = {}
    with open(filename, "r") as handle:
        for line in handle.readlines():
            line_content = line.split()
            for codon, aa in zip(line_content[::2], line_content[1::2]):
                code[codon] = aa
    return code

def translate(rna, genetic_code_file):
    code = make_genetic_code(genetic_code_file)
    protein = []
    for i in range(0, len(rna), 3):
        protein.append(code[rna[i:i+3]])
    return "".join(protein)

def test_translate(data_file, genetic_code_file):
    with open(data_file, "r") as handle:
        rna = handle.readline().strip()
    print(translate(rna, genetic_code_file))

test_translate("data/rosalind_prot.txt", "data/genetic_code.txt")
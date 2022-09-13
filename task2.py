def dna_to_rna(dna):
    result = []
    for i in list(dna):
        result.append(i.replace('T', 'U'))
    return ''.join(result)

print(dna_to_rna("GCAT"))

def DNAtoRNA(dna):
    return dna.replace('T', 'U')
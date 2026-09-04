def rna(dna):
    rna = ''
    reverse = ''
    dna = list(dna)

    for i in dna:
        if i == "T":
            i = "U"
        reverse += i

    rna = reverse[::-1]

    return rna

'''
def rna(dna):
    rna = ''
    dna = list(dna)
    
    for i in dna:
        if i == "A":
            rna += "U"
        elif i == "T":
            rna += "A"
        elif i == "C":
            rna += "G"
        elif i == "G":
            rna += "C"

    return rna
'''
#the problem asked to change T for U and reverse but some searchs said that A>U, T>A, C>G and G>C. idk...

print(rna("ATCG"))
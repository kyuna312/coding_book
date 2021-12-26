from rosalind_utils import mass_to_aa

def build_peptide(l, peptide='', aa=0):

    if aa == 0:
        aa = min(l)
    
    if aa not in l:
        return peptide
    else:
        for i in l[aa]:
            return build_peptide(l, peptide+i[0], i[1])
    

def peptide_from_spectrum(l):
    # amino
    # acids.
    pairs = {}
    for i in range(len(l)):
        for j in range(i, len(l)):
            aa = mass_to_aa(l[j]-l[i])
            if aa:
                if l[i] in pairs:
                    pairs[l[i]].append((aa, l[j]))
                else:
                    pairs[l[i]] = [(aa, l[j])]
        
    peptide = build_peptide(pairs)
    
    # peptide length n.
    return peptide
        

def main():
    with open('./rosalind_sgra.txt', 'r') as infile:
        l = list(map(float, infile.readlines()))
    
    print(peptide_from_spectrum(l))


if __name__ == '__main__':
    main()
#!/usr/bin/python

from rosalind_utils import aa_mass
from decimal import *
getcontext().prec = 8

def possible_masses(p):
    # Calculate peptide.
    masses = []
    
    for i in range(len(p)):
        masses.append(Decimal(aa_mass(p[:i])))
        masses.append(Decimal(aa_mass(p[i:])))

    return masses
    
    
def multiplicity(s, t):
    # Calculate Minkowski difference .
    sets = {}
    
    for i in s:
        for j in t:
            d = i - j
            if d in sets:
                sets[d] += 1
            else:
                sets[d] = 1

    largest = max((v, k) for k, v in sets.items())
    
    return largest
    

def main():
    most_occurances = 0
    most_peptide = ''
    

    with open('./rosalind_prsm.txt', 'r') as infile:
        n = int(infile.readline())
        peptides = [infile.readline().strip() for i in range(n)]
        spectrum = [Decimal(i) for i in infile.readlines()]


    for i in peptides:
        occurances, k = multiplicity(possible_masses(i), spectrum)
        
        if occurances >= most_occurances:
            most_occurances = occurances
            most_peptide = i
    
    print(most_occurances, '\n', most_peptide, sep='')
    

if __name__ == '__main__':
    main()

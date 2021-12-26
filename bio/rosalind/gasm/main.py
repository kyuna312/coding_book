#!/usr/bin/python

from rosalind_utils import reverse_complement as rc
from itertools import chain

def cyclic_superstring(dna):
    flatten = lambda listOfLists: chain.from_iterable(listOfLists)
    
    n = len(dna)
    l = len(dna[0])  # assumes all strings are the same length
    
    for k in range(l-1, 1, -1):
        adj = dict(flatten([[(d[i:i+k], d[i+1:i+k+1]) for i in range(l-k)] for d in dna]))
        first = kmer = next(iter(adj))
        superstring = ''
        
        while True:
            if kmer in adj:
                superstring += kmer[-1]
                kmer = adj.pop(kmer)
                if kmer == first:
                    return superstring
            else:
                break


def main():
    with open('./rosalind_gasm.txt', 'r') as infile:
        dna = infile.read().strip().split('\n')
        dna = list(set(dna + [rc(i) for i in dna])) # Add the reverse complement of each string.
    
    with open('./rosalind_gasm_out.txt', 'w') as outfile:
        outfile.write(cyclic_superstring(dna))
    

if __name__ == '__main__':
    main()

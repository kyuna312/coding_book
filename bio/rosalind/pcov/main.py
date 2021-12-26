#!/usr/bin/python

def adjacency_list(seq_list):
    # kmers.
    kmers_in_seq = lambda seq: (seq[:-1], seq[1:])
    
    # sequence haih
    kmers = {}
    for seq in seq_list:
        for k in kmers_in_seq(seq):
            if k in kmers:
                kmers[k].append(seq)
            else:
                kmers[k] = [seq]
                
    # De Bruijn tree.
    adjacency = {}
    for kmer, seqs in kmers.items():
        for seq in seqs:
            for k in kmers_in_seq(seq):
                if kmer[1:] == k[:-1]:
                    adjacency[kmer] = k
    
    return adjacency
    

def cyclic_superstring(dna):
    adj = adjacency_list(dna)
    
    first = next(iter(adj.keys()))
    superstring = first
    
    prev = adj[superstring]
    
    while prev != first:
        superstring += prev[-1]
        prev = adj[prev]
    
    i = len(superstring)//2
    while i < len(superstring):
        if superstring[i:] == superstring[:len(superstring)-i]:
            superstring = superstring[:i]
            break
        i += 1

    return superstring


def main():
    with open('./rosalind_pcov.txt', 'r') as infile:
        dna = infile.read().strip().split('\n')
    
    with open('./rosalind_pcov_out.txt', 'w') as outfile:
        outfile.write(cyclic_superstring(dna))
    

if __name__ == '__main__':
    main()
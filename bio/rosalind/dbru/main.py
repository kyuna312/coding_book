from rosalind_utils import reverse_complement as rc
from collections import defaultdict

def de_bruijn(seq_list):
    seq_list = list(set(seq_list + [rc(i) for i in seq_list]))

    kmers_in_seq = lambda seq: (seq[:-1], seq[1:])
    
    kmers = defaultdict(list)
    for seq in seq_list:
        for k in kmers_in_seq(seq):
            kmers[k].append(seq)
    
    adjacency = defaultdict(set)
    for kmer, seqs in kmers.items():
        for seq in seqs:
            for k in kmers_in_seq(seq):
                if kmer[1:] == k[:-1]:
                    adjacency[kmer].add(k)
    
    return adjacency
    
    
def main():
    with open('./rosalind_dbru.txt', 'r') as infile:
        s = infile.read().strip().split('\n')
    
    answer = de_bruijn(s)
    
    with open('./rosalind_dbru_out.txt', 'w') as outfile:
        for i in answer:
            for j in answer[i]:
                outfile.write('(' + i + ', ' + j + ')\n')
    
    
if __name__ == '__main__':
    main()
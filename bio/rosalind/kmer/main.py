#!/usr/bin/python
from itertools import product

def count_mers(seq, k=4):
    mer_dict = {i:0 for i in [''.join(j) for j in list(product('ACGT', repeat=k))] }
    
    for i in range(len(seq)-k+1):
        mer_dict[seq[i:i+k]] += 1

    return mer_dict


def composition(seq):
    mer_dict = count_mers(seq)

    array = []
    for i in sorted(mer_dict):
        array.append(mer_dict[i])

    array = ' '.join([str(i) for i in array])
    
    return array


def main():
    with open('./rosalind_kmer.txt', 'r') as infile:
        seq = ''.join(infile.readlines()[1:]).replace('\n', '')

    with open('./rosalind_kmer_out.txt', 'w') as outfile:
        outfile.write(composition(seq))

    
if __name__ == '__main__':
    main()

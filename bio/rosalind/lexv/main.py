#!/usr/bin/python
from itertools import product

def generate_strings(alpha, n):
    strings = []
    for i in range(1, n+1):
        strings += [''.join(j) for j in product(alpha, repeat=i)]

    strings = sorted(strings, key=lambda s: [alpha.index(ch) for ch in s])
    
    return strings


def main():
    with open('./rosalind_lexv.txt', 'r') as infile:
        alpha = infile.readline().strip().split(' ')
        n = int(infile.readline())

    strings = generate_strings(alpha, n)
    
    with open('./rosalind_lexv_out.txt', 'w') as outfile:
        outfile.write('\n'.join(strings))


if __name__ == '__main__':
    main()

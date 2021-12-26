#!/usr/bin/python

if __name__ == '__main__':
    with open('./rosalind_sset.txt', 'r') as infile:
        n = int(infile.read())

    print(2**n % 1000000)

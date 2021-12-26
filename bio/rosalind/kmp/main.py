#!/usr/bin/python
from rosalind_utils import parse_fasta

def failure_array(s):
    f = [0 for i in range(len(s))]
    n = len(s)
    k = 1 
    j = 0 

    while k < n:
        if s[k] == s[j]:
            j += 1
            f[k] = j
            k += 1
        else:
            if j != 0:
                j = f[j-1]
            else:
                f[k] = 0
                k += 1

    return f


def main():
    s = parse_fasta('./rosalind_kmp.txt')
    
    with open('./rosalind_kmp_out.txt', 'w') as outfile:
        outfile.write(' '.join(map(str, failure_array(s))))


if __name__ == '__main__':
    main()

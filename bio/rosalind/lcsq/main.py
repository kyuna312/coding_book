#!/usr/bin/python
from rosalind_utils import parse_fasta

def build_matrix(s, t, m, n):
    d = [[[] for x in range(n+1)] for y in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                d[i][j] = 0
            elif s[i-1] == t[j-1]:
                d[i][j] = d[i-1][j-1]+1
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])
    
    return d


def longest_sub(s, t):
    i = len(s)
    j = len(t)
    table = build_matrix(s, t, i, j)

    seq = ''
    while i>0 and j>0:
        if s[i-1] == t[j-1]:
            seq = s[i-1] + seq
            i -= 1
            j -= 1
        elif table[i-1][j] > table[i][j-1]:
            i -= 1
        else:
            j -= 1

    return seq
    
        
def main():
    s, t = parse_fasta('./rosalind_lcsq.txt')
    seq = longest_sub(s, t)

    with open('./rosalind_lcsq_out.txt', 'w') as outfile:
        outfile.write(seq)

    print('The longest common subsequence is', len(seq), 'bases long.')
        

if __name__ == '__main__':
    main()

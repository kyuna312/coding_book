#!/usr/bin/python


from rosalind_utils import parse_fasta, BLOSUM62, match_score

def global_align(s, t, matrix, gap):

    # match  mismatch onoo.
    M = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    # gap matrits .
    X = [[-9999 for j in range(len(t)+1)] for i in range(len(s)+1)]
    Y = [[-9999 for j in range(len(t)+1)] for i in range(len(s)+1)]

    
    for i in range(1, len(s)+1):
        M[i][0] = gap
    for j in range(1, len(t)+1):
        M[0][j] = gap

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            X[i][j] = max([M[i-1][j] + gap,
                           X[i-1][j]])
            Y[i][j] = max([M[i][j-1] + gap,
                           Y[i][j-1]])
            M[i][j] = max([M[i-1][j-1] + match_score(matrix, s[i-1], t[j-1]),
                           X[i][j],
                           Y[i][j]])
    
    return M[-1][-1]


def main():
    s, t = parse_fasta('./rosalind_gcon.txt')
    max_score = global_align(s, t, BLOSUM62(), -5)
    
    print(max_score)
    

if __name__ == '__main__':
    main()

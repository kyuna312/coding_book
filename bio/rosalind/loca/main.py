#!/usr/bin/python
from rosalind_utils import parse_fasta, PAM250, match_score
    
def alignment_score(s, t, scores, gap):
    S = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    traceback = [[3 for j in range(len(t)+1)] for i in range(len(s)+1)]

    best = 0
    best_pos = (0, 0)

    # matrices.
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            cost = [ S[i-1][j-1] + match_score(scores, s[i-1], t[j-1]),
                     S[i-1][j] + gap,
                     S[i][j-1] + gap,
                     0 ]
            S[i][j] = max(cost)
            traceback[i][j] = cost.index(S[i][j])

            if S[i][j] >= best:
                best = S[i][j]
                best_pos = (i, j)

    i, j = best_pos

    r, u = s[:i], t[:j]
    
    while traceback[i][j] != 3 and i*j != 0:
        if traceback[i][j] == 0: # match
            i -= 1
            j -= 1
        elif traceback[i][j] == 1: # insertion
            i -= 1
        elif traceback[i][j] == 2: # deletion
            j -= 1

    r = r[i:]
    u = u[j:]

    return str(best), r, u


def main():
    s, t = parse_fasta('./rosalind_loca.txt')
    alignment = alignment_score(s, t, PAM250(), -5)

    with open('./rosalind_loca_out.txt', 'w') as outfile:
        outfile.write('\n'.join(alignment))

    print('Max alignment score =', alignment[0])


if __name__ == '__main__':
    main()

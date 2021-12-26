#!/usr/bin/python

from rosalind_utils import parse_fasta, BLOSUM62, match_score
    
def local_align_with_affine(s, t, scores, gap, gap_e):
    # Initialize the arrays that will contain the previous round of scores.
    Sx = [0 for i in range(len(t)+1)]
    Sy = [0 for j in range(len(t)+1)]
    Sm = [0 for i in range(len(t)+1)]
    
    # Initialize the traceback matrix.
    traceback = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    best = -1
    best_pos = (0, 0)

    # Fill in the Score and Traceback matrices.
    for i in range(1, len(s)+1):
        new_x = [0 for i in range(len(t)+1)]
        new_y = [0 for i in range(len(t)+1)]
        new_m = [0 for i in range(len(t)+1)]
        
        for j in range(1, len(t)+1):
            new_x[j] = max([Sm[j] + gap, Sx[j] + gap_e])
            new_y[j] = max([new_m[j-1] + gap, new_y[j-1] + gap_e])
            costM = [Sm[j-1] + match_score(scores, s[i-1], t[j-1]),
                     new_x[j],
                     new_y[j],
                     0]
            new_m[j] = max(costM)
            traceback[i][j] = costM.index(new_m[j])

            if new_m[j] > best:
                best = new_m[j]
                best_pos = i, j

        Sx = new_x
        Sy = new_y
        Sm = new_m
    
    # Initialize the values of i, j
    i, j = best_pos
    
    # Initialize the aligned strings as the input strings.
    r, u = s[:i], t[:j]

    # Traceback to build alignment.
    while traceback[i][j] != 3 and i*j != 0:
        if traceback[i][j] == 0:
            i -= 1
            j -= 1
        elif traceback[i][j] == 1:
            i -= 1
        elif traceback[i][j] == 2:
            j -= 1
   
    r = r[i:]
    u = u[j:]
    
    return str(best), r, u


def main():
    s, t = parse_fasta('./rosalind_laff.txt')
    alignment = local_align_with_affine(s, t, BLOSUM62(), -11, -1)
    
    with open('./rosalind_laff_out.txt', 'w') as outfile:
        outfile.write('\n'.join(alignment))

    print('Maximum alignment score =', alignment[0])


if __name__ == '__main__':
    main()

from rosalind_utils import parse_fasta, BLOSUM62, match_score

def global_align(s, t, scores, gap):
    S = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

    for i in range(1, len(s)+1):
        S[i][0] = i * gap
    for j in range(1, len(t)+1):
        S[0][j] = j * gap

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            S[i][j] = max([ S[i-1][j-1] + match_score(scores, s[i-1], t[j-1]),
                            S[i-1][j] + gap,
                            S[i][j-1] + gap ])

    return S[-1][-1]

   
def main():
    s, t = parse_fasta('./rosalind_glob.txt')
    max_score = global_align(s, t, BLOSUM62(), -5)
    
    print(max_score)
        

if __name__ == '__main__':
    main()

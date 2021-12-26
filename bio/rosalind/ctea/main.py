from rosalind_utils import parse_fasta

def count_alignments(s, t):
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    counts = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    for i in range(0, len(s)+1):
        d[i][0] = i
        counts[i][0] = 1
    for j in range(1, len(t)+1):
        d[0][j] = j
        counts[0][j] = 1
    
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            scores = [d[i-1][j-1] + (s[i-1] != t[j-1]),
                      d[i-1][j] + 1,
                      d[i][j-1] + 1]
            d[i][j] = min(scores)

            if d[i][j] == scores[0]: counts[i][j] += counts[i-1][j-1]
            if d[i][j] == scores[1]: counts[i][j] += counts[i-1][j]
            if d[i][j] == scores[2]: counts[i][j] += counts[i][j-1]
            counts[i][j] = counts[i][j] % 134217727
    
    return counts[-1][-1]


def main():
    s, t = parse_fasta('./rosalind_ctea.txt')
    print(count_alignments(s, t))


if __name__ == '__main__':
    main()

from rosalind_utils import parse_fasta
    
def edit_dist(s, t):
    m, n = len(s), len(t)
    
    d = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        d[i][0] = i
    for j in range(1, n+1):
        d[0][j] = j

    for j in range(1, n+1):
        for i in range(1, m+1):
            if s[i-1] == t[j-1]:
                d[i][j] = d[i-1][j-1]           # a match
            else:
                d[i][j] = min(d[i-1][j] + 1,    # a deletion
                              d[i][j-1] + 1,    # an insertion
                              d[i-1][j-1] + 1)  # a substitution 
    edit_dist = d[m][n]
    
    return edit_dist


def main():
    s, t = parse_fasta('./rosalind_edit.txt')
    
    print(edit_dist(s, t))
    

if __name__ == '__main__':
    main()

from rosalind_utils import parse_fasta

def edit_dist_with_align(s, t):
    d = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    traceback = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]

    for i in range(1, len(s)+1):
        d[i][0] = i
    for j in range(1, len(t)+1):
        d[0][j] = j


    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            scores = [d[i-1][j-1] + (s[i-1] != t[j-1]), 
                      d[i-1][j] + 1,                    
                      d[i][j-1] + 1]                    
            d[i][j] = min(scores)
            traceback[i][j] = scores.index(d[i][j])
            
    edit_dist = d[-1][-1]
    
    s_align, t_align = s, t

    i, j = len(s), len(t)
    
    while i>0 and j>0:
        if traceback[i][j] == 1:
            i -= 1
            t_align = t_align[:j] + '-' + t_align[j:]
        elif traceback[i][j] == 2:
            j -= 1
            s_align = s_align[:i] + '-' + s_align[i:]
        else:
            i -= 1
            j -= 1

    for dash in range(i):
        t_align = t_align[:0] + '-' + t_align[0:]
    for dash in range(j):
        s_align = s_align[:0] + '-' + s_align[0:]

    return edit_dist, s_align, t_align

   
def main():
    s, t = parse_fasta('./rosalind_edta.txt')
    aligned = edit_dist_with_align(s, t)

    with open('./rosalind_edta_out.txt', 'w') as outfile:
        outfile.write('\n'.join(map(str, aligned)))

    print('Edit distance =', aligned[0])
        

if __name__ == '__main__':
    main()

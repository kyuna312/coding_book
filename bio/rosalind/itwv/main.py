from itertools import combinations_with_replacement as comb_r

def is_superstring(a, b, superstr):    
    # Check if two strings can be interwoven into a superstring.
    if len(superstr) == 0:
        return True
    elif a[0] == b[0] == superstr[0]:
        return is_superstring(a[1:], b, superstr[1:]) or is_superstring(a, b[1:], superstr[1:])
    elif a[0] == superstr[0]:
        return is_superstring(a[1:], b, superstr[1:])
    elif b[0] == superstr[0]:
        return is_superstring(a, b[1:], superstr[1:])
    else:
        return False
    
    
def find_disjoint_motifs(s, patterns):
    matrix = [[0 for j in range(len(patterns))] for i in range(len(patterns))]
    
    for i in list(comb_r((i for i in range(len(patterns))), 2)):
        a = patterns[i[0]]
        b = patterns[i[1]]
 
        for j in range(len(s)-len(a)-len(b)+1):
            superstr = s[j:j+len(a)+len(b)]

            if is_superstring(a+'$', b+'$', superstr):

                matrix[i[0]][i[1]] = 1
                matrix[i[1]][i[0]] = 1
                break

    return matrix


def main():
    with open('./rosalind_itwv.txt', 'r') as infile:
        s = infile.readline().strip()
        patterns = infile.read().strip().split('\n')

    matrix = find_disjoint_motifs(s, patterns)

    with open('./rosalind_itwv_out.txt', 'w') as outfile:
        for i in matrix:
            outfile.write(' '.join(map(str, i)) + '\n')

    for i in matrix:
        print(' '.join(map(str, i)))
        

if __name__ == '__main__':
    main()

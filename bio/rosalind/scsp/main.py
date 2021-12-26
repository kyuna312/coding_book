from rosalind_lcsq import longest_sub

def shortest_sub(s, t):
    lcs = longest_sub(s, t)
    
    scs = [''] * (len(lcs)+1)

    m = 0
    n = 0
    for i in range(len(lcs)):
        while s[m] != lcs[i] and m < len(s):
            scs[i] += s[m]
            m += 1
        while t[n] != lcs[i] and n < len(t):
            scs[i] += t[n]
            n += 1

        scs[i] += lcs[i]
        m += 1
        n += 1

    scs[-1] = s[m:] + t[n:]
   
    return ''.join(scs)
    
        
def main():
    with open('./rosalind_scsp.txt', 'r') as infile:
        s, t = infile.read().strip().split('\n')

    seq = shortest_sub(s, t)
    
    with open('./rosalind_scsp_out.txt', 'w') as outfile:
        outfile.write(seq)
        
    print('shortest common supersequence =', seq)
        

if __name__ == '__main__':
    main()

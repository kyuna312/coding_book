def gc_p(seq, gc):
    percent = 1
    prob_gc = gc/2
    prob_at = (1-gc)/2
    
    for j in range(len(seq)):
        nt = seq[j]
        if nt == 'G' or nt == 'C':
            percent = percent * prob_gc
        elif nt == 'A' or nt == 'T':
            percent = percent * prob_at

    return(percent)


def prob(n, s, a):
    for i in a:
        prob = gc_p(s, i) * (n-1)
        yield(prob)

    
def main():
    with open('./rosalind_eval.txt', 'r') as infile:
        n, s, a = infile.read().strip().split('\n')
        n = int(n)
        a = [float(i) for i in a.split(' ')]

    print(' '.join(['%.3f' % p for p in prob(n, s, a)]))

if __name__ == '__main__':
    main()

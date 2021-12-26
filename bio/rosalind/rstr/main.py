#!/usr/bin/python
def prob(n, gc, seq):
    percent = 1
    prob_gc = gc/2
    prob_at = (1-gc)/2
    
    for i in seq:
        if i == 'G' or i == 'C':
            percent *= prob_gc
        elif i == 'A' or i == 'T':
            percent *= prob_at

    percent = 1 - (1 - percent) ** n
    
    return percent

    
def main():
    with open('./rosalind_rstr.txt', 'r') as infile:
        n, s = infile.read().strip().split('\n')
        n, x = n.split(' ')
        n = int(n)
        x = float(x)

    print('%.3f' % prob(n, x, s))


if __name__ == '__main__':
    main()

from math import sqrt

def probability(i):
    p = sqrt(i)
    q = 1 - p
    prob = (2 * p * q) + i
    return prob

def main():
    with open('./rosalind_afrq.txt', 'r') as infile:
        a = [float(i) for i in infile.read().strip().split(' ')]
    prob = [probability(i) for i in a]

    with open('./rosalind_afrq_out.txt', 'w') as outfile:
        outfile.write(' '.join(['%.3f' % i for i in prob]))

if __name__ == '__main__':
    main()

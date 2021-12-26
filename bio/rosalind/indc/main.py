from math import log10, factorial as f

def binomial_random_variable(n, k, p):
    a = f(n) / f(k) / f(n-k)  # binomial coefficient
    b = p**k * (1-p)**(n-k)
    c = a * b
    
    return c


def main():
    n = int(open('./rosalind_indc.txt').read())
    prob = [binomial_random_variable(n*2, k, 0.5) for k in range(2*n, -1, -1)]
    
    prob = [log10(sum(prob[:i])) for i in range(2*n, 0, -1)]
    
    with open('./rosalind_indc_out.txt', 'w') as outfile:
        outfile.write(' '.join([str(i) for i in prob]))
        

if __name__ == '__main__':
    main()

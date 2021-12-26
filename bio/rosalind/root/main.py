if __name__ == '__main__':
    doublefactorial = lambda n: n * doublefactorial(n-2) if n > 1 else 1 
    n = int(open('./rosalind_root.txt', 'r').read())
    
    print(doublefactorial(2*n-3) % 1000000)

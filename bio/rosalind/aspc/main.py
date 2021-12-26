from math import factorial as f

def combinations(n, m):
    return sum(f(n) // (f(k) * f(n-k)) for k in range(m, n+1))


def main():
    with open('./rosalind_aspc.txt', 'r') as infile:
        n, m = [int(i) for i in infile.readline().strip().split(' ')]


    answer = combinations(n, m) % 1000000
    print(answer)


if __name__ == '__main__':
    main()

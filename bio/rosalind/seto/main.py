def main():
    with open('./rosalind_seto.txt', 'r') as infile:
        n = int(infile.readline().strip())
        a = set(map(int, infile.readline().strip()[1:-1].split(', ')))
        b = set(map(int, infile.readline().strip()[1:-1].split(', ')))
        
    with open('./rosalind_seto_out.txt', 'w') as outfile:
        answer = (set.union(a, b), 
                  set.intersection(a, b),
                  set.difference(a, b),
                  set.difference(b, a),
                  set.difference(set(range(1, n+1)), a),
                  set.difference(set(range(1, n+1)), b))
        outfile.write('\n'.join(map(str, answer)))


if __name__ == '__main__':
    main()

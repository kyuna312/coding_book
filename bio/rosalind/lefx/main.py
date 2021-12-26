import itertools

with open("./rosalind_lexf.txt", 'r') as f:
    string = f.readline().split()
    n = int(f.readline().strip())
    result = list(itertools.product(string, repeat = n))
    print("\n".join(["".join(x) for x in result]))
    
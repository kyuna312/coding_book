# ^_^ coding:utf-8 ^_^


def Permutation(n):
    import itertools
    list1 = []
    for i in range(n):
        list1.append(i + 1)
    list2 = list(itertools.permutations(list1, n))
    print(len(list2))
    for l in list2:
        print(" ".join([str(i) for i in l]))

if __name__ == "__main__":
    with open("./rosalind_perm.txt", "r") as f:
        n = int(f.readline().strip())
    Permutation(n)

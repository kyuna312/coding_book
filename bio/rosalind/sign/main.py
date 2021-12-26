# ^_^ coding:utf-8 ^_^

import itertools

def SignedPermutation(n):
    list1 = []
    for i in range(n):
        list1.extend([i + 1, - i - 1])
    list2 = list(itertools.permutations(list1, n))

    list3 = []
    for a in list2:
        aset = set()
        for i in a:
            aset.add(abs(i))
        if len(aset) < len(a):
            list3.append(a)

    list4 = list(set(list2) ^ set(list3))
    print(len(list4))
    for i in list4:
        a = str(i)
        a = a.replace('(', '').replace(',', '').replace(')', '')
        print(a)

if __name__ == "__main__":
    with open("./rosalind_sign.txt", "r") as f:
        n = int(f.readline().strip())
        SignedPermutation(n)

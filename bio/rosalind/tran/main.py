f = open("rosalind_tran.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

def tAndT(s1, s2):
    t1 = 0
    t2 = 0

    for i in range(0, len(s1)):
        if (s1[i] != s2[i]):
            if (s1[i] == 'A' and s2[i] == 'G'):
                t1 = t1 + 1
            elif (s1[i] == 'G' and s2[i] == 'A'):
                t1 = t1 + 1
            elif (s1[i] == 'C' and s2[i] == 'T'):
                t1 = t1 + 1
            elif (s1[i] == 'T' and s2[i] == 'C'):
                t1 = t1 + 1
            else:
                t2 = t2 + 1
    return t1 / t2

s1, s2 = mat
print(tAndT(s1, s2))
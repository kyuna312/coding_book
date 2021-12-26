def factorial(n):
    f = 1
    for i in range(1, n+1):
        f  = f *i
    return f

def combination(i, j):
    return factorial(i)/(factorial(j) * factorial(i - j))

def independent_alleles(k, n):
    p = 0
    count = pow(2, k)                        # count 为第k代人数
    for i in range(n, count+1):
        p += combination(count, i) * pow(0.25, i) * pow(0.75, count - i)
    return p

if __name__ == "__main__":
    with open("./rosalind_lia.txt", "r") as f:
        k, n = [int(i) for i in f.readline().strip().split(" ")]
    print(independent_alleles(k,n))
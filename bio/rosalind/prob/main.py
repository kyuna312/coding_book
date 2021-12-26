import math

with open("./rosalind_prob.txt", "r") as f:
    s = f.readline().strip()
    A = map(float, f.readline().strip().split(" "))

a = s.count('A') + s.count('T')
c = s.count('C') + s.count('G')
for i in A:
    p = a * math.log((1-i)/2, 10) + c * math.log(i/2, 10)
    print(p, end=" ")
    
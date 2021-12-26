# ^_^ utf-8: ^_^


with open("./rosalind_inod.txt") as f:
    n = int(f.readline().strip())
# n = 4
print("the number of internal nodes is:", n-2)
print("the total number of the tree nodes is:", 2*n-2)
print("the edges of the tree is:", n-1)

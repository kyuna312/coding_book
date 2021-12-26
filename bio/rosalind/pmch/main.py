# ^_^ coding:utf-8 ^_^
from Bio import SeqIO

def factorial(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return f

def pmch(s):
    a = s.count('A')
    c = s.count('C')
    print(a, c)
    return factorial(a) * factorial(c)
if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open ("./rosalind_pmch.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    string = seq_string[0]
    print(pmch(string))

# ^_^ coding: utf-8 ^_^

from Bio import SeqIO

seq_name, seq_string = [], []
with open("./rosalind_pdst.txt", "r") as fa:
	for seq_record in SeqIO.parse(fa, "fasta"):
		seq_name.append(str(seq_record.name))
		seq_string.append(str(seq_record.seq))

def p_distance(s1, s2):
    n = len(s1)
    m = 0
    for i in range(n):
        if s1[i] != s2[i]:
            m += 1
    return '%.5f'% (float(m)/n)

for i in range(len(seq_name)):
    for j in range(len(seq_name)):
        print(p_distance(seq_string[i],seq_string[j]), end=" ")
    print('')

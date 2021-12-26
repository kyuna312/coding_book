# ^_^ coding:utf-8 ^_^


def mrna(protein):
    codons = {'F': ['UUU', 'UUC'],
              'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'Y': ['UAU', 'UAC'],
              '*': ['UAA', 'UAG', 'UGA'],
              'C': ['UGU', 'UGC'],
              'W': ['UGG'],
              'P': ['CCU', 'CCC', 'CCA', 'CCG'],
              'H': ['CAU', 'CAC'],
              'Q': ['CAA', 'CAG'],
              'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
              'V': ['GUU', 'GUC', 'GUA', 'GUG'],
              'A': ['GCU', 'GCC', 'GCA', 'GCG'],
              'D': ['GAU', 'GAC'],
              'E': ['GAA', 'GAG'],
              'G': ['GGU', 'GGC', 'GGA', 'GGG'],
              'I': ['AUU', 'AUC', 'AUA'],
              'M': ['AUG'],
              'T': ['ACU', 'ACC', 'ACA', 'ACG'],
              'N': ['AAU', 'AAC'],
              'K': ['AAA', 'AAG']}
    number = 1
    for aa in protein:
        number = number * len(codons[aa])
    number = number*len(codons["*"])
    return number % 1000000


if __name__ == "__main__":
    with open("./rosalind_mrna.txt", 'r') as f:
        protein = f.readline().strip()
        number = mrna(protein)
        print(number)

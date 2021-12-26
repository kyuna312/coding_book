rna_to_aminoacid_dictionary =  {'UUU' : 'F', "UUC": 'F', 'UUA' : 'L', 'UUG' : 'L', 'UCU' : 'S' , 'UCA' :'S', 'UCC' : 'S', 'UCG' : 'S', 'UAU' : 'Y', 'UAC': 'Y', 'UAA': 'STOP' , 'UAG': 'STOP', 'UGU' : 'C', 'UGC': 'C', 'UGA' : 'STOP', 'UGG': 'W', 'CUU' : 'L', 'CUC' : 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'CAU' : 'H', 'CAC':'H', 'CAA':'Q','CAG':'Q','CGU': 'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'I','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G'}

file = open("rosalind_splc.txt", "r")

def extract_sequence_from_input(file):
    sequences = []
    result = ""       
    
    for line in file:
        if ">" in line:
            sequences.append(result)
            result = ""
        else:
            if "\n" in line:
                result += line[:len(line) - 1]
            else:
                result += line
    sequences.append(result)

    sequences.remove('')
    return sequences

sequences = extract_sequence_from_input(file)


dna_string = sequences[0]

introns = sequences[1:]

introns.sort(reverse = True)


for intron in introns:
    dna_string = dna_string.replace(intron,"")
dna_string = dna_string.replace("T","U")

for i in range(0, len(dna_string) - 3, 3):
    print(rna_to_aminoacid_dictionary[dna_string[i: i +3]],end='')
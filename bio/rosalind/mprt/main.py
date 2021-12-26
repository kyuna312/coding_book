# import urllib
# from urllib.request import urlopen
# import os
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# from urllib.request import urlopen
# import re

# filenames = []
# sequences = []
# f = open('rosalind_mprt.txt', 'r')
# for l in f:
#     l = l.replace('\n', '')
#     filename = l + '.txt'    
#     filenames.append(l)
#     urllib.request.urlretrieve('http://www.uniprot.org/uniprot/' + l + '.fasta', filename)
#     f1 = open(filename, 'r')
#     counter = 0    
#     line = ''    
#     for l1 in f1:
#         if counter != 0:
#             line += l1
#         counter += 1    
#         line = line.replace('\n', '')
#     sequences.append(line)
#     f1.close()
#     os.remove(filename)

# res = []
# for s in sequences:
#     positions = ''    
#     for i in range(0, len(s)-3):
#         if s[i] == 'N':
#             if s[i+1] != 'P':
#                 if s[i+2] == 'S' or s[i+2] == 'T':
#                     if s[i+3] != 'P':
#                         pos = i+1                        
#                         positions += str(pos) + ' '    
#                         res.append(positions)

# for q in range(len(filenames)):
#     if len(res[q]) > 0:
#         print(filenames[q])
#         print(res[q])

import re
import requests

#arquivo = open('/home/augusto/Downloads/rosalind_mprt.txt','r')
arquivo = open('./rosalind_mprt.txt','r')
entradas =  arquivo.read().strip().split('\n')

#print entradas

for entrada in entradas:
    r = requests.get('http://www.uniprot.org/uniprot/%s.fasta' % entrada)
    proteina = r.text
    enter = proteina.find('\n')
    proteina = proteina[(enter+1):]
    proteina = proteina.replace('\n','')
    busca = re.finditer('(?=(N[^P][ST][^P]))',proteina)
    saida=[]
    for i in busca:
        saida.append(i.start()+1)
        #print i.start()+1,
        #print proteina[i.start():i.start()+4]
    if len(saida)>0:
        print (entrada)
        for i in saida:
            print (i),
        print()
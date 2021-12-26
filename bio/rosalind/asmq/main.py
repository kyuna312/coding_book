#!/usr/bin/python


def Nxx(lenlist, xx):

    n = 100 / (100 - xx)
    medianpos = int(len(lenlist) / n)
    print (medianpos)
    if len(lenlist) % 2 == 0:
        return lenlist[medianpos] + lenlist[medianpos-1] / n
    else:
        return lenlist[medianpos]


def main():
    with open('./rosalind_asmq.txt', 'r') as infile:
        dna = infile.read().strip().split('\n')

    # Create a list containing n copies of an integer, n, where n is the
    # length of each given string in a list.
    lenlist = []
    for i in dna:
        lenlist += [len(i)]*len(i)
    lenlist = sorted(lenlist)
    print (len(lenlist))

    print(Nxx(lenlist, 50), Nxx(lenlist, 75))


if __name__ == '__main__':
    main()

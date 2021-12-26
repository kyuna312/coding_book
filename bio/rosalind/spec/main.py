from rosalind_utils import mass_to_aa

def calc_protein(l):
    prot = ''
    for i in range(1, len(l)):
        prot += mass_to_aa(l[i]-l[i-1])
        
    return prot


def main():
    # Read in the list of prefix weights.
    with open('./rosalind_spec.txt', 'r') as infile:
        l = list(map(float, infile.read().strip().split('\n')))

    # Print answer.
    print(calc_protein(l))
        

if __name__ == '__main__':
    main()

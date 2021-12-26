from decimal import Decimal

def largest_multiplicity(s, t):
    sets = {}
    for i in s:
        for j in t:
            d = i - j
            if d in sets:
                sets[d] += 1
            else:
                sets[d] = 1
    
    largest = max((v, k) for k ,v in sets.items())
    
    return largest
    
    
def main():
    with open('./rosalind_conv.txt', 'r') as infile:
        s, t = [[Decimal(x) for x in line.split()] for line in infile.read().strip().split('\n')]      
        
    print('\n'.join(map(str, largest_multiplicity(s, t))))
    
if __name__ == '__main__':
    main()
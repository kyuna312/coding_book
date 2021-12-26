import re

def parse_taxa(t):
    return sorted(re.sub('[^0-9a-zA-Z_]+', ' ', t).strip().split(' '))
    

def char_table_from_newick(t):
    char = []
    
    taxa = parse_taxa(t)
    taxa_dict = {i:taxa.index(i) for i in taxa}
    
    level = 0
    pos = []
    subtrees = []
    
    for i in range(len(t)):
        if t[i] == '(':
            level += 1
            pos.append(i)
        elif t[i] == ')':
            sub = t[pos[-1]+1:i]
            del pos[-1]

            while len(subtrees) < level:
                subtrees.append([])
                
            subtrees[level-1].append(sub)
            level -= 1
    
    for i in range(1, len(subtrees)):
        for j in subtrees[i]:
            char.append([0 for i in range(len(taxa_dict))])
            
            for k in parse_taxa(j):
                char[-1][taxa_dict[k]] = 1
    
    return char
    
    
def main():
    with open('./rosalind_ctbl.txt', 'r') as infile:
        tree = infile.read().strip()
    
    answer = char_table_from_newick(tree)
    
    with open('./rosalind_ctbl_out.txt', 'w') as outfile:
        outfile.write('\n'.join([''.join(map(str, answer[i])) for i in range(len(answer))]))


if __name__ == '__main__':
    main()
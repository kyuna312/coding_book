def longest_substring(s, k, edges):

    child = {}
    parent = {}
    for p, c, a, b in edges:
        t = s[int(a)-1:int(a)-1+int(b)]

        if p in child:
            child[p].append(c)
        else:
            child[p] = [0, c]
        
        if c in parent:
            parent[c].append(p)
        else:
            parent[c] = [0, t, p]
    
    # Find the root of the tree.
    for i in child.keys():
        if i not in parent:
            root = i
    
    # Find the leaves (childless nodes) of the tree.
    leaves = []
    for i in parent.keys():
        if i not in child:
            leaves.append(i)

    # Annotate the levels of the tree (i.e. distance from root).
    p = [root]
    lvl = 1
    while True:
        new_p = []
        for i in p:
            if i in child:
                for j in child[i][1:]:
                    parent[j][0] += lvl
                    new_p.append(j)

        if new_p != []:
            p = new_p
            lvl += 1
        else:
            break

    # Count the number of leaf descendants of each node.
    top_nodes = []
    for i in leaves:
        top = ''
        par = parent[i][2]
        
        while True:
            child[par][0] += 1
            
            if child[par][0] >= k:
                if par != root:
                    top_nodes.append(par)
                
            if par in parent:
                par = parent[par][2]
            else:
                break

    # Find the max depth of the nodes w/ at least k leaf descendants.
    max_depth = max([parent[i][0] for i in top_nodes])

    # ...of those nodes, get the one(s) farthest from the root.
    deep_nodes = []
    for i, j in parent.items():
        if j[0] == max_depth:
            if i not in leaves:
                deep_nodes.append(i)

    # Traceback to the root to build substrings.
    substrings = []
    for i in deep_nodes:
        sub = ''
        par = i
        while True:
            t, par = parent[par][1:]
            sub = t + sub
            if par not in parent:
                substrings.append(sub)
                break

    # Return the longest of the substrings.
    longest = max(substrings, key=len)
    
    return longest

            
def main():
    with open('./rosalind_lrep.txt', 'r') as infile:
        s = infile.readline().strip()
        k = int(infile.readline().strip())
        edges = [i.strip().split(' ') for i in infile.readlines()]
    
    print(longest_substring(s, k, edges))
    
    
if __name__ == '__main__':
    main()

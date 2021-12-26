def pair(seq):
    # seq  length 
    if len(seq) < 4:
        return 1
    
    if seq in prev:
        return prev[seq]
        
    else:
        prev[seq] = pair(seq[1:])
        
        for i in range(4, len(seq)):
            if seq[i] in match[seq[0]]:
                prev[seq] += pair(seq[1:i]) * pair(seq[i+1:])
    
    return prev[seq]
    
    
if __name__ == '__main__':
    # Read sequence.
    with open('./rosalind_rnas.txt', 'r') as infile:
        seq = infile.read().replace('\n', '')
        
    match = {'A':'U', 'U':'AG', 'C':'G', 'G':'CU'}

    prev = {}
    
    # Print answer.
    print(pair(seq))s
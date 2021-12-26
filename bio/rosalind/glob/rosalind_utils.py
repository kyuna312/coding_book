def parse_fasta(path, no_id=True):
    ids = []
    seqs = []
    
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                ids.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()

    if no_id == True:
        if len(seqs) > 1:
            return seqs
        else:
            return seqs[0]
    else:
        return dict(zip(ids, seqs))

def BLOSUM62():
    return scoring_matrix('./blosum62.txt')


def scoring_matrix(path):
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')

    scores = [lines[0].split()] + [l[1:].split() for l in lines[1:]]

    return scores


def match_score(scoring_matrix, a, b):
    x = scoring_matrix[0].index(a)
    y = scoring_matrix[0].index(b)
    cost = int(scoring_matrix[x+1][y])

    return cost

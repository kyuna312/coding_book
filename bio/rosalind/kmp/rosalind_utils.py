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


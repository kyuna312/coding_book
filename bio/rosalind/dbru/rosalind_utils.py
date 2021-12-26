def reverse_complement(seq):
    if 'U' in seq:
        seq_dict = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
    else:
        seq_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

    return ''.join([seq_dict[base] for base in reversed(seq)])


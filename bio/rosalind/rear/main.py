#!/usr/bin/python

def split_pair(pair):
    p1, p2 = [list(map(int, p.split(' '))) for p in pair]
    
    return p1, p2


def breakpoint(p):
    bp = []
    for i in range(1, len(p)):
        if abs(p[i] - p[i-1]) > 1:
            bp.append(i)
    
    return bp


def printRound(p, a, b):
    if 10 in p[a:b]:
        x = 1
    else:
        x = 2
        
    print(p, ' - ', '(', a, ',', b-1, ')', sep='')
    print(' ', ' '*(a*3), '-'*((b-a)*3-x), sep='')


def reversal_dist(p1, p2):
    if p1 == p2:
        return(0)
    
    p_start = [0] + [p1.index(x)+1 for x in p2] + [len(p1)+1]
    #print('-'*50, '\n', p_start, ' <-- reverse\n', sep='')

    perm_list = [p_start]
    bp_min = len(breakpoint(p_start))

    count = 0
    while count < len(p_start)+1:
        #print('Round #%i' % int(count+1))
        new_perms = []

        count += 1

        for perm in perm_list:
            bp = breakpoint(perm)
            for i in range(len(bp)):
                for j in range(i+1, len(bp)):
                    a = bp[i]
                    b = bp[j]
                    if b-a > 1:

                        p_new = perm[:a] + list(reversed(perm[a:b])) + perm[b:]
                        bp_new = len(breakpoint(p_new))


                        if bp_new == 0:
                            #print('breakpoints = %i' % bp_new)
                            #printRound(p_new, a, b)
                            return count
                        elif bp_new < bp_min:
                            #print('breakpoints = %i' % bp_new)
                            #printRound(p_new, a, b)
                            bp_min = bp_new
                            new_perms = [p_new]
                        elif bp_new == bp_min:
                            #printRound(p_new, a, b)
                            new_perms.append(p_new)

        perm_list = new_perms


def main():
    with open('./rosalind_rear.txt', 'r') as infile:
        permutations = [x.split('\n') for x in infile.read().strip().split('\n\n')]
        permutations = [split_pair(pair) for pair in permutations]

    counts = [min(reversal_dist(pair[0], pair[1]),
                  reversal_dist(pair[1], pair[0])) for pair in permutations]

    print(' '.join(map(str, counts)))


if __name__ == '__main__':
    main()

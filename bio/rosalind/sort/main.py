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
        return 0

    p_start = [0] + [p1.index(x)+1 for x in p2] + [len(p1)+1]
    
    count = 0
    reversal_list = [[[p_start, count]]]
    bp_min = len(breakpoint(p_start))

    while count < len(p_start)+1:
        reversal_list.append([])
        new_reversals = []
        
        for perm_item in reversal_list[count]:
            perm = perm_item[0]
            revs = perm_item[2:]
            bp = breakpoint(perm)

            for i in range(len(bp)):
                for j in range(i+1, len(bp)):
                    a = bp[i]
                    b = bp[j]
                    if b-a > 1:

                        p_new = perm[:a] + list(reversed(perm[a:b])) + perm[b:]
                        bp_new = len(breakpoint(p_new))

                        if len(perm_item)>2:
                            revs = perm_item[2:][0]+[a]+[b-1]
                        else:
                            revs = [a,b-1]

                        if bp_new == 0:
                            return p_new, count+1, revs
                        elif bp_new < bp_min:
                            bp_min = bp_new
                            reversal_list[count+1] = []
                            reversal_list[count+1].append([p_new, count+1, revs])
                        elif bp_new == bp_min:
                            reversal_list[count+1].append([p_new, count+1, revs])

        count += 1


def checkAnswer(to_match, to_reverse, revs):

    temp = to_reverse
    for i in range(0, len(revs), 2):
        a = revs[i]-1
        b = revs[i+1]
        
        printRound(temp, a, b)
        temp = temp[:a] + list(reversed(temp[a:b])) + temp[b:]

    if temp == to_match:
        print(temp, '<-- Correct Match!\n')
    else:
        print(temp, '<-- Incorrect Match!\n')

    
def main():
    # Read the input .txt file.
    with open('./rosalind_sort.txt', 'r') as infile:
        pair = infile.read().strip().split('\n')
        permA, permB = [list(map(int, p.split(' '))) for p in pair]

    perm, count, revs = reversal_dist(permA, permB)

    print(count)
    for i in range(len(revs), 0, -2):
        print(revs[i-2], revs[i-1])


if __name__ == '__main__':
    main()

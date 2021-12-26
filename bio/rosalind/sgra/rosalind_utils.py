def aa_mass(aa):
    mass_table = { 'A':71.03711,
                   'C':103.00919,
                   'D':115.02694,
                   'E':129.04259,
                   'F':147.06841,
                   'G':57.02146,
                   'H':137.05891,
                   'I':113.08406,
                   'K':128.09496,
                   'L':113.08406,
                   'M':131.04049,
                   'N':114.04293,
                   'P':97.05276,
                   'Q':128.05858,
                   'R':156.10111,
                   'S':87.03203,
                   'T':101.04768,
                   'U':150.95363,
                   'V':99.06841,
                   'W':186.07931,
                   'Y':163.06333 }
                   
    aa = aa.upper()
    
    if 'B' in aa:
        print('Ambiguity: B can be either Asparagine (N) or Aspartic acid (D)!')
        return None
    if 'Z' in aa:
        print('Ambiguity: Z can be either  Glutamine (Q) or Glutamic acid (E)!')
        return None
        
    mass = 0
    for i in aa:
        try:
            mass += mass_table[i]
        except KeyError:
            print('Error: Could not find a mass for an amino acid %s.' % i)
            return None
    
    return mass


def mass_to_aa(val, tolerance=0.0001):
    aa_table = { 71.03711:'A',
                 103.00919:'C',
                 115.02694:'D',
                 129.04259:'E',
                 147.06841:'F',
                 57.02146:'G',
                 137.05891:'H',
                 113.08406:'I',
                 128.09496:'K',
                 113.08406:'L',
                 131.04049:'M',
                 114.04293:'N',
                 97.05276:'P',
                 128.05858:'Q',
                 156.10111:'R',
                 87.03203:'S',
                 101.04768:'T',
                 150.95363:'U',
                 99.06841:'V',
                 186.07931:'W',
                 163.06333:'Y' }
    
    closest = ['', 999]
    
    for mass, aa in aa_table.items():
        diff = abs(val - mass)
        if diff < closest[1]:
            closest = [aa, diff]
            
        if diff < tolerance:
            return aa

    print('Note: Could not find an amino acid with monoisotopic mass %.5f.' % val)
    print(' '*6 + 'Closest match is', closest[0], '(mass difference %5f).' % closest[1])



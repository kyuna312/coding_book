
def mass_to_aa(val, tolerance=0.0001):
    ''' Returns the amino acid corresponding to a given mass. '''
    
    # The monoisotopic masses of each 
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
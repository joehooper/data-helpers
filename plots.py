'''Helper functions for plotting'''

def bin_list(i, n, c=0):
    '''Generate a list of integers to define bins for plotting

    Keyword arguments:
    i -- size of bin
    n -- number of bins
    c -- center of bin range (default 0)
    Note that the number of bins must always be even.
    If n is odd, the number of bins will be n-1.
    for example bin_list(2,5,1) = [-3, -1, 1, 3, 5]
    '''
    b = int(n/2*-1)
    e = int((-1*b) + 1)
    return [ (x*i)+c for x in range(b,e)]
    

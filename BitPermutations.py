"""
David Schonberger
Hackerrank.com
Combinatorics - Bit permutations
1/17/2015
"""

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
    
T = input()
for i in range(T):
    ar = raw_input()
    ar = ar.split(' ')
    ar = [int(x) for x in ar]
    n = ar[0]
    m = ar[1]
    print ncr(n + m - 1, n) % (10**9 + 7)
    
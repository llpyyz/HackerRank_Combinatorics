"""
David Schonberger
Hackerrank.com
Combinatorics - nCr table
1/17/2015
"""
import operator as op

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

##Note: take only last 9 (or fewer digits if ans > 9 digits)
T = input()
for i in range(T):
    n = input()
    for i in range(n + 1):
        r = ncr(n,i)
        if(r >= 10**9):
            r %= 10**9
        print r,
    print

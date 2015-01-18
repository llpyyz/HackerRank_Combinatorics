"""
David Schonberger
Hackerrank.com
Combinatorics - Candy Store (-combination from set with n elements, rep allowed)
1/17/2015
"""
import operator as op

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

#Note: take only last 9 (or fewer digits if ans > 9 digits)
T = input()
for i in range(T):
    N = input()
    K = input()
    ans = str(ncr(N + K - 1, K))
    if(len(ans) > 9): 
        ans = ans[len(ans) - 9:]
    print int(ans)


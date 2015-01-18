"""
David Schonberger
Hackerrank.com
Combinatorics - Chocolate Fiesta (Counting subsets)
1/17/2015
"""

import operator as op

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def pow_mod_m(base, exp, mod):
    ret = 1
    for i in range(exp):
        ret = (ret * base)
        if(ret >= mod):
            ret = ret % mod
    return ret
    
N = input()
ar = raw_input()
ar = ar.split(' ')
ar = [int(x) for x in ar]

even_count = len([x for x in ar if x % 2 == 0])
odd_count = len([x for x in ar if x % 2 == 1])
modulus = 10**9 + 7
odd_subset_count = 0
if(odd_count > 1):
    odd_subset_count += pow(2 , odd_count-1 , modulus) - 1
    
subset_count = (pow_mod_m(2,even_count , modulus) * (1 + odd_subset_count) - 1) % modulus

print subset_count

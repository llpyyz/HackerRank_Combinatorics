"""
David Schonberger
Hackerrank.com
Combinatorics - DiwaliLights (Counting subsets II)
1/17/2015
"""


def pow_mod_m(base, exp, mod):
    ret = 1
    for i in range(exp):
        ret = (ret * base)
        if(ret >= mod):
            ret = ret % mod
    return ret
    
T = input()
mod = 10**5
for i in range(T):
    N = input()
    print pow_mod_m(2 , N , mod) - 1
    

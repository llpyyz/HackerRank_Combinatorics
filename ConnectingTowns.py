"""
David Schonberger
Hackerrank.com
Search - Connecting Towns (Fundamental counting principle)
1/17/2015
"""

T = input()
for i in range(T):
    n = input()
    ar = raw_input()
    ar = ar.split(' ')
    ar = [int(x) for x in ar]
    prod = 1
    for elt in ar:
        prod = (prod * elt) % 1234567
    print prod

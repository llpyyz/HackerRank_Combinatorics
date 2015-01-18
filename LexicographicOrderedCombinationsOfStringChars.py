"""
David Schonberger
Hackerrank.com
Combinatorics - Building a List (lexicographic ordering of combs)
1/18/2015
"""

import itertools

T = input()
for i in range(T):
    n = input()
    s = raw_input()
    l = []
    for i in range(1, len(s) + 1):
        lst = list(itertools.combinations(s,i))
        for tup in lst:
            tmp = ''
            for elt in tup:
                tmp += elt
            l.append(tmp)
    l.sort()
    for elt in l:
        print elt
        


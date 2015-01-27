"""
David Schonberger
Hackerrank.com
Combinatorics - Picking cards
1/21/2015
"""

mod = 10**9 + 7
T = input()
for i in range(T):
    n = input()
    ar = raw_input()
    ar = ar.split(' ')
    ar = [int(x) for x in ar]
    ar.sort()
    counts = []
    j = 0
    curr = 0
    prev = 0
    while(j < n):
        c = 0
        while(j < n and ar[j] == curr):
            j += 1
            c += 1
        counts.append(c + prev)
        prev = counts[len(counts) - 1]
        curr += 1
    if(len(counts) < n):
        m = counts[len(counts) - 1]
        for j in range(n - len(counts)):
            counts.append(m)
    counts = [max(0, counts[i] - i) for i in range(len(counts))]    
    if(0 in counts):
        prod = 0
    else:
        prod = 1
        for j in range(len(counts)):
            prod *= counts[j]
            if(prod >= mod):
                prod %= mod
                
    print prod  

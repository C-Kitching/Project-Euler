#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    res = -1
    for a in range(1, n//3):
        b = (n**2 - 2*a*n)//(2*(n-a))
        c = n - a - b
        if(a**2 + b**2 == c**2):
            res = max(res, a*b*c)
    print(int(res))

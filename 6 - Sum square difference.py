#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_squ = (n*(n+1)/2)**2
    squ_sum = n*(n+1)*(2*n+1)/6
    print(int(abs(sum_squ - squ_sum)))

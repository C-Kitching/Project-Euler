#!/bin/python3

import sys

# create sorted list of all three digit product palindromes
palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        p = i*j
        if str(p) == str(p)[::-1] and p not in palindromes:
            palindromes.append(p)
palindromes = sorted(palindromes, reverse = True) 

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # check all paldinromes
    for p in palindromes:
        # print first one less than n
        if(p < n):
            print(p)
            break

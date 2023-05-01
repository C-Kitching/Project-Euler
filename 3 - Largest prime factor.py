#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largest_prime = -1
    i = 2
    while(i*i <= n):
        while(n%i == 0):
            largest_prime = i
            n /= i
        i += 1
    if(n > 1): largest_prime = n
    print(int(largest_prime))

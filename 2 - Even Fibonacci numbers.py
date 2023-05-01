#!/bin/python3

import sys

cases = int(input().strip())

for case in range(cases):
    N = int(input().strip())
    res = 0
    fib_nums = [1, 2]
    even_fibs = [2]
    while(fib_nums[-1] + fib_nums[-2] < N):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
        if(fib_nums[-1]%2 == 0): even_fibs.append(fib_nums[-1])
    print(sum(even_fibs))

# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

def build_num(size, pos, digits):
    num = 0
    for i in range(1, size+1):
        num *= 10
        num += digits[pos]
        pos += 1
    return num, pos

n = int(input())
digits = list(range(1, n+1))

perms = list(itertools.permutations(digits))
pandigitals = set()

sum_pandigitals = 0

# loop through lengths of each number
for digits in perms:
    for a in range(1, n):
        for b in range(1, n-a):
            
            # determine c length
            c = n - a - b
            
            # the product cant have shorter length than either
            if(c < a or c < b): continue
            
            # contains currently used position in digits
            pos = 0
            
            # determine the numbers
            a_num, pos = build_num(a, pos, digits)
            b_num, pos = build_num(b, pos, digits)
            c_num, pos = build_num(c, pos, digits)
            
            # if pandigital and not product seen before
            if(a_num*b_num == c_num and c_num not in pandigitals):
                sum_pandigitals += c_num
                pandigitals.add(c_num)
            
print(sum_pandigitals)
            
        
            
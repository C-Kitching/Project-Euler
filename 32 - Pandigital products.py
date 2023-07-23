import itertools
from itertools import permutations

def contains_pandigital_prod(perm, N):

    # join the permutation into a string
    num = ''.join(str(i) for i in perm)

    if num == "391867254":
        x = 5

    # loop over all slicings into 3 numbers
    for i in range(1, N-1):
        for j in range(i+1, N):
            a = int(num[:i])
            b = int(num[i:j])
            c = int(num[j:])

            # if it is pandigital product
            if(a*b == c):
                return True
            
    return False


# read input
N = int(input())

# form the root pandigital number
num = list(range(1, N+1))

# determine all permutations
perms = list(permutations(num))

count_pandigital_prods = 0

# loop over all pandigitals
for perm in perms:

    # count the number which are panditial products
    if contains_pandigital_prod(perm, N):
        count_pandigital_prods += 1

print(count_pandigital_prods)
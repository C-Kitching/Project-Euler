# Enter your code here. Read input from STDIN. Print output to STDOUT

MAX_NUM = 10**5

amicable_sums = [0] * (MAX_NUM+1)

# sum proper divisors of N
# note that all numbers except 0 and 1 have 1 as a proper divisor
divisor_sums = [0, 0] + [1] * MAX_NUM  
for divisor in range(2, MAX_NUM//2):
    for num in range(2*divisor, MAX_NUM + 1, divisor):
        divisor_sums[num] += divisor

# sum all amicable numbers below N
amicable_sums = [0] * (MAX_NUM+1)
for i in range(1, MAX_NUM+1):
    amicable_sums[i] = amicable_sums[i-1]
    if divisor_sums[i] <= MAX_NUM and divisor_sums[i] != i and divisor_sums[divisor_sums[i]] == i:
        amicable_sums[i] += i

for _ in range(int(input())):
    n = int(input())
    print(amicable_sums[n])
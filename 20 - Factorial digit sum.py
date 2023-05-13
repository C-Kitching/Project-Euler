# Enter your code here. Read input from STDIN. Print output to STDOUT

def sum_of_digits_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    sum_of_digits = 0
    for digit in str(fact):
        sum_of_digits += int(digit)
    return sum_of_digits

for _ in range(int(input())):
    N = int(input())
    print(sum_of_digits_factorial(N))

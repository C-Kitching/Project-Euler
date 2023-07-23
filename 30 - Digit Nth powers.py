
import math

def find_upper_bound(N):
    """Find upper bound on the number that could be the sum of its digits,
    each raised to the Nth power. It can be determined via the formulae
    10^(d-1) <= d*9^N < 10^d
    Solving gives
    d - log10(d) <= 5.77 < d - log10(d) + 1

    Args:
        N (int): power to raise digits to
    """

    d = 1
    while True:
        if d - math.log10(d) > 5.77: 
            max_digits = d-1
            break
        d += 1

    return int(max_digits*math.pow(9, N))

def sum_powers_of_digits(num, N):
    """Sum over the powers of the digits of a number

    Args:
        num (int): number we want to sum
        N (int): power to raise digits to

    Returns:
        float: sum of power raised digits
    """
    sum = 0
    for i in str(num):
        sum += int(i)**N
    return sum

def main():
    """Main function
    """

    # read in data
    N = int(input())

    # set bounds on search space
    lower_bound = 10
    upper_bound = find_upper_bound(N)

    # sum all possible numbers
    res = 0 
    for num in range(lower_bound, upper_bound + 1):
        if num == sum_powers_of_digits(num, N):
            res += num

    print(res)

# driver code 
if __name__ == "__main__":
    main()


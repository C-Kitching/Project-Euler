# Enter your code here. Read input from STDIN. Print output to STDOUT

#RELEVANT RESOURCES
#https://oeis.org/A007732
#https://math.stackexchange.com/questions/377683/length-of-period-of-decimal-expansion-of-a-fraction/1207111

def calculate_longest_cycle_d(N):
    """For every number in the range [1, N], determine the number d with the 
    largest recipricol decimal cycle

    Args:
        N (int): maximum d to check

    Returns:
        int[]: the ith element gives the value of d < i+1 that has the longest
        recipricol decimal cycle
    """
    

    # initialise with d = 3
    # because it is the first repeating decimal
    max_length_and_corresponding_d = [1, 3]
    longest_cycle_d = [0, 0, 0, 0]

    # start search from 4
    for d in range(4, N+1):

        # if divisor is divisable by 2 or 5
        # then this cycle is no longer than the previously found max
        if d%2==0 or d%5==0:
            longest_cycle_d.append(max_length_and_corresponding_d[1])

        else:

            # we store max before current as we want d < N
            longest_cycle_d.append(max_length_and_corresponding_d[1])

            # find the value of n such that (10^n)mod(d) = 1
            # Note that using the pow function is too expensive
            # modular arithmetic is faster by noting
            # (a*b)mod(d) = ((a)mod(d))*(b)mod(d)
            # so *10 %d repeated n times is equivilant to doing (10^n)mod(d)
            l = 1
            rem = 1
            while True:
                rem *= 10
                rem %= d
                if rem == 1: break
                l += 1

            # if it is longer than the current max
            if l > max_length_and_corresponding_d[0]:
                max_length_and_corresponding_d = [l, d]

    return longest_cycle_d

# determine the d < N that has the longest cycle
longest_cycle_d = calculate_longest_cycle_d(10000)

for _ in range(int(input())):
    N = int(input())

    print(longest_cycle_d[N])


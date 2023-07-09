# Enter your code here. Read input from STDIN. Print output to STDOUT

#RELEVANT RESOURCES
#https://oeis.org/A007732
#https://math.stackexchange.com/questions/377683/length-of-period-of-decimal-expansion-of-a-fraction/1207111


# calculate the decimal lengths of the first N numbers
def calculate_cycle_lengths(N):
    """Calculate the decnimal length of the first N 1/d numbers

    Args:
        N (int): number of fractions to calculate for

    Returns:
        int[]: index i is the decimal length of 1/(i+1)
    """

    cycle_lengths = []
    for d in range(1, N+1):

        # if divisor is divisable by 2 or 5
        if d%2==0 or d%5==0:

            # factor out 2 and 5
            if d%2 == 0: d /= 2
            if d%5 == 0: d /= 2

            # length of cycle is then the same as the length of cylce of new d
            # this is because 1/(2^i*5^j*d) has the same cycle length as 1/d
            cycle_lengths.append(cycle_lengths[int(d)-1])

        else:
            # find the value of n such that (10^n-1)mod(d) = 0
            n = 1
            while True:
                if (pow(10, n) - 1)%d == 0: 
                    cycle_lengths.append(n)
                    break
                n += 1

    return cycle_lengths

def determine_longest_cycle_d(cycle_lengths):

    # initalise longest cycle as 0
    max_length_and_d = [1, 3]
    longest_cycle_d = []

    # go through all d and l values
    for i, l in enumerate(cycle_lengths):

        # update max length
        if l > max_length_and_d[0]:
            max_length_and_d = [l, i+1]

        # store d belonging to longest cycle seen so far
        longest_cycle_d.append(max_length_and_d[1])

    return longest_cycle_d


# calculate cycle lengths of first N 1/d fractions
cycle_lengths = calculate_cycle_lengths(100)

# determine the d < N that has the longest cycle
longest_cycle_d = determine_longest_cycle_d(cycle_lengths)

for _ in range(int(input())):
    N = int(input())

    print(longest_cycle_d[N-1])




    
    
    
    
    
    
    
    
    


def count_distinct_powers(N):
    """For all a and b pairs in the range [2, N], count the number of unique
    a^b, for example 2^4 = 4^2 so 16 is not a unique power

    Args:
        N (int): upper bound
    """

    count = 0
    tested = [0]*(N+1)

    # loop through all bases
    for base in range(2, N+1):

        # if we have already looked at this base continue to next
        if tested[base]: continue

        # This set holds sets of exponents for each power of the base
        # For example if base = 2, then its first power is 2^2 = 4
        # All powers of 4 can be written as powers of 2 (N=5 e.g): 
        # 4^2 = 2^4, 4^3 = 2^6, 4^4 = 2^8, 4^5 = 2^10
        # Thus the exponents for this power of 2 are [4,6,8,10]
        # Note that these are just the multiples of the first power, 2
        # We are only interested in multiples larger than N
        # With N = 5 we would only take [6, 8, 10] for this set
        # Because they represent unique powers of 4, as we cannot have
        # 2^6, 2^8 or 2^10 as the powers are > 5
        exponents_for_base = set()

        # start with the smallest power
        power = 2

        # Now loop through all powers that are smaller than our upper bound N
        # This is because the powers will be used as bases when calculating 
        # the set of exponents and both the base and power must be <= N
        while(base**power <= N):

            # mark that we have now tested the new base given by base**power
            # so we can skip it in future
            tested[base**power] = True

            # since we skip the base, base**power in future
            # we determine the number of unique elements that it would produce
            # this is simply the multiples of power that are larger than N
            # mutiples that are smaller than N are not unique
            # E.g power=2, N = 5, the multiples are: 4,6,8,10
            # and only one of which is <= N
            exponents_for_base_power = set([n*power for n in range(2, N+1) if n*power > N])

            # update the exponents for the base with the exponents for the base power
            # each of these exponents represents a duplicate power that will appear
            exponents_for_base.update(exponents_for_base_power)

            # move to the next power
            power += 1

        # incrememnt the count
        # N-1 represents the raw powers of the base, for example if base = 2 and N = 5
        # we have 2^2, 2^3, 2^4, 2^5 i.e [2,3,4,5] or N-1 = 5-1 = 4 distinct powers
        # The length of the set represents the unique powers that will occur 
        # in the bases that we are going to skip. 
        # For example the first power of base = 2 was 4, we will skip base = 4
        # so we need to know which powers of 4 are unique
        # In this case only 4^4, 4^4 and 4^5 as 4^2 = 2^4 so we have an additional 3
        # Since 4 is the only base**power<=5 that is skipped, in this example
        # we get a contribution of N-1 3 times, plus the additional 3
        # giving a result of 15
        count += len(exponents_for_base) + N-1

    return count



N = int(input())
print(count_distinct_powers(N))
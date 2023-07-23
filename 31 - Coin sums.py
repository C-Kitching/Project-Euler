# all british coins
coins = [1,2,5,10,20,50,100,200]

# initailise a dynamic programming array
upper_bound = 10**5
dp = [0] * (upper_bound+1)
dp[0] = 1

# loop over all coin values
for coin in coins:

    # check every target value
    for target in range(coin, upper_bound):

        # number of ways to reach target is the number of ways to reach 
        # the target subtract the current coin as we just add the current coin
        dp[target] += dp[target - coin]

# loop over all possibl
# handle all test cases
for _ in range(int(input())):
    N = int(input())

    print(dp[N]%(10**9+7))
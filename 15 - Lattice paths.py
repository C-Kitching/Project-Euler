# Enter your code here. Read input from STDIN. Print output to STDOUT

# dynamic programming to precompute all possible paths
dp = [[0 for i in range(500)] for j in range(500)]
for i in range(500):
    for j in range(500):      
        if i != 0 and j != 0:
            dp[i][j] = int((dp[i][j-1] + dp[i-1][j])%(1e9+7))
        elif i == 0 or j == 0:
            dp[i][j] = 1

T = int(input())
for _ in range(T):
    row, col = input().split()
    row = int(row)
    col = int(col)
    print(dp[col][row])

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = 0
N = int(input())
for _ in range(N):
    s += int(input())
    
print(str(s)[:10])

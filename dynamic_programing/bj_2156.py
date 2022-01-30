import sys
input = sys.stdin.readline

n = int(input())
li = [0]
for _ in range(n):
    li.append(int(input()))

if n<3:
    print(sum(li))
else:
    dp = [0] * (n+1)
    dp[1] = li[1]
    dp[2] = li[1] + li[2]

    for i in range(3, n+1):
        c1 = li[i] + li[i-1] + dp[i-3]
        c2 = li[i] + dp[i-2]
        c3 = dp[i-1]
        dp[i] = max(c1, c2, c3)
    print(dp[n])
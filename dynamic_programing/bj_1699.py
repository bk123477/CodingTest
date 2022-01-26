import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)
sqr = [i*i for i in range(1, 317)]

for i in range(1, n+1):
    s = []
    for j in sqr:
        if j > i:
            break
        s.append(dp[i-j])
    dp[i] = min(s) + 1
print(dp[n])
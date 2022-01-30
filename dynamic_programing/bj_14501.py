import sys
from time import time

n = int(sys.stdin.readline().rstrip())
timeTable = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + timeTable[i][0] > n: # 범위 넘어가면 N+1일꺼
        dp[i] = dp[i+1]
    # N+1일의 수익과 N + Tn의 수익 중 큰 값    
    else:
        dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i+1])

print(dp[0])
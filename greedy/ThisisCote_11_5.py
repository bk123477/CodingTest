import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
weight = list(map(int, input().rstrip().split()))
weight.sort()

result = 0
prev = 0
dp = [0] * (m+1)

for w in weight:
    dp[w] += 1

for i in range(1, len(dp)-1):
    temp = 0
    for j in range(i+1, len(dp)):
        temp += dp[j]
    
    result += temp * dp[i]

print(result)

# sol) 이것도 맞지만 이중 반복문을 없애려면 다음과 같이 변형
# for i in range(1, m+1):
#     n -= dp[i]
#     result += dp[i] * n
# print(result)
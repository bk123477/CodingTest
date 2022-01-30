import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
dp = [-1] * (100001)
c_list = set()
for i in range(n):
    c_list.add(int(input().rstrip()))
coin_list = list(c_list)
coin_list.sort()

for coin in coin_list:
    dp[coin] = 1

for i in range(1, k+1):
    if i < dp[coin_list[0]]:
        continue
    else:
        temp = []
        for coin in coin_list:
            if i-coin>0 and dp[i-coin] != -1:
                temp.append(dp[i-coin])
            elif i-coin == 0:
                temp.append(0)
        if len(temp) > 0:
            dp[i] = min(temp) + 1
print(dp[k])
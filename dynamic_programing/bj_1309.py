import sys

n = int(sys.stdin.readline().rstrip())
dp = [[0]*3 for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1
for i in range(1, n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901 # i번째에 사자 없는경우
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901 # i번째에 사자 왼쪽
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901 # i번째에 사자 오른쪽 -> %9901 미리 하는이유는 숫자가 너무 커져서 미리 나머지연산 하는거임
print((dp[n-1][0] + dp[n-1][1] + dp[n-1][2]) % 9901)
import sys

n = int(sys.stdin.readline().rstrip())

result = [0] * 1001
result[1] = 1
result[2] = 2
for i in range(3, n+1):
    result[i] = (result[i-2] + result[i-1]) % 10007
print(result[n]%10007)
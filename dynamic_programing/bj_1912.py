import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))
result = [0 for _ in range(n)]
result[0] = li[0]
for i in range(1, n):
    if result[i-1] < 0:
        result[i] = li[i]
    else:
        result[i] = result[i-1] + li[i]
print(max(result))
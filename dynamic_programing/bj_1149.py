import sys

n = int(sys.stdin.readline().rstrip())
li = [[0]* 3 for _ in range(n)]
for i in range(n):
    li[i] = (list(map(int, sys.stdin.readline().rstrip().split())))
result = [[0]*3 for _ in range(n)]
result[0][0] = li[0][0]
result[0][1] = li[0][1]
result[0][2] = li[0][2]
# result[n번째][r,g,b]
for i in range(1, n):
    result[i][0] = li[i][0] + min(result[i-1][1], result[i-1][2])
    result[i][1] = li[i][1] + min(result[i-1][0], result[i-1][2])
    result[i][2] = li[i][2] + min(result[i-1][0], result[i-1][1])
print(min(result[n-1][0],result[n-1][1],result[n-1][2]))
import sys

triangle = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = [[0] * n for _ in range(n)]
result[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(i+1):
        l, r = 0, 0
        if j-1 >= 0:
            l = result[i-1][j-1]
        if j <= i-1:
            r = result[i-1][j]
        result[i][j] = max(l, r) + triangle[i][j]

print(max(result[n-1]))
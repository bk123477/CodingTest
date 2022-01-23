import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
result_maps = []
for _ in range(n):
    result_maps.append(list(map(int, sys.stdin.readline().rstrip())))

cnt = 0
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if result_maps[i][j] == 1:
            for a in range(i+1):
                for b in range(j+1):
                    result_maps[a][b] = 1 - result_maps[a][b]
            cnt += 1
print(cnt)
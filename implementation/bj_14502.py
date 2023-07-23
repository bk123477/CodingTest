# acmicpc.net/problem/14502

import sys
from itertools import combinations
import copy
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus():
    global result
    for wall_combination in combinations(wall_location, 3):
        test_map = copy.deepcopy(graph)
        for x_w, y_w in wall_combination:
            test_map[x_w][y_w] = 1
        
        virus_location = [(n, m) for n in range(N) for m in range(M) if test_map[n][m] == 2]
        while virus_location:
            x_v, y_v = virus_location.pop()
            for i in range(4):
                nx = x_v + dx[i]
                ny = y_v + dy[i]
                if 0 <= nx < N and 0 <= ny < M and test_map[nx][ny] == 0:
                    test_map[nx][ny] = 2
                    virus_location.append((nx, ny))
        cnt = 0
        for row in test_map:
            cnt += row.count(0)
        result = max(result, cnt)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
wall_location = [(n, m) for n in range(N) for m in range(M) if graph[n][m] == 0]

result = 0
virus()
print(result)
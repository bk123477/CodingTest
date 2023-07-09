# acmicpc.net/problem/18405

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

graph = [] # 전체 보드 정보 담는 리스트
data = [] # 바이러스에 대한 정보 담는 리스트
for i in range(N):
    graph.append(list(map(int, input().rstrip().split())))
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호 바이러스 먼저 증식
data.sort()
q = deque(data)

S, X, Y = map(int, input().rstrip().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    # S초가 지나거나, 큐가 빌 때까지 반복
    if s == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[X-1][Y-1])
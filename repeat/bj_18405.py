# acmicpc.net/problem/18405

import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

test = []
for _ in range(N):
    test.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


next = []
for i in range(N):
    for j in range(N):
        if test[i][j] > 0:
            heapq.heappush(next, (test[i][j], i, j)) # virusNum, x, y

print("next", next)

for t in range(S):
    current=[[0]*N for _ in range(N)]
    while next:
        virusNum, x, y = heapq.heappop(next)
        current[x][y] = virusNum
    visit = [[False] * N for _ in range(N)]
    
    while current:
        virusNum, x, y = heapq.heappop(current)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and test[nx][ny] == 0 and not visit[nx][ny]:
                visit[nx][ny] = True
                test[nx][ny] = virusNum
                heapq.heappush(next, (test[nx][ny], nx, ny))
    print("next", next)
print(test)
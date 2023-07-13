# acmicpc.net/problem/4485

import sys
import heapq
input = sys.stdin.readline
INF = 1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []
while True:
    N = int(input())
    
    if N == 0:
        break
    else:
        cave = []
        for _ in range(N):
            cave.append(list(map(int, input().split())))
        distance = [[INF] * N for _ in range(N)]
        visit = [[False] * N for _ in range(N)]
        start_x, start_y = 0, 0
        q = []
        heapq.heappush(q, (cave[start_x][start_y], start_x, start_y))
        visit[0][0] = True
        distance[0][0] = cave[0][0]
        while q:
            cost, cur_x, cur_y = heapq.heappop(q)
            if distance[cur_x][cur_y] < cost:
                continue
            for i in range(4):
                nx, ny = cur_x + dx[i], cur_y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if not visit[nx][ny]:
                    c = distance[cur_x][cur_y] + cave[nx][ny]
                    distance[nx][ny] = c
                    visit[nx][ny] = True
                    heapq.heappush(q, (c, nx, ny))
        result.append(distance[N-1][N-1])

for i in range(len(result)):
    print("Problem %d: %d" %(i+1, result[i]))
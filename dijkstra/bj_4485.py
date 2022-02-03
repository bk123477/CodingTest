import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] # 상, 하, 좌 우
result = []

while True:
    n = int(input().rstrip())
    if n == 0: break
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    distance = [[INF for _ in range(n)] for _ in range(n)]
    visited=[[False for _ in range(n)] for _ in range(n)]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0)) # 루피, x좌표, y좌표
    distance[0][0] = graph[0][0]
    visited[0][0] = True
    while q:
        loopy, yloc, xloc = heapq.heappop(q)
        if distance[yloc][xloc] < loopy:
            continue
        for i in range(4):
            next_y = yloc + dy[i]
            next_x = xloc + dx[i]
            if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n:
                continue
            if not visited[next_y][next_x]:
                cost = distance[yloc][xloc] + graph[next_y][next_x]
                if cost < distance[next_y][next_x]:
                    distance[next_y][next_x] = cost
                    visited[next_y][next_x] = True
                    heapq.heappush(q, (cost, next_y, next_x))
    result.append(distance[n-1][n-1])
for i in range(len(result)):
    print('Problem %d: %d' %(i+1, result[i]))
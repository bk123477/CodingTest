# acmicpc.net/problem/18352
# bfs 방식으로 못 풀었음. 옛날엔 dijkstra로 풀었었음. 나중에 다시 풀기.

import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9

# input : N : 도시 개수, M : 도로 개수, K : 거리 정보, X : 출발 도시 번호
# output : 최단 거리가 정확히 K인 도시의 번호 출력
N, M, K, X = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0

queue = deque([X])
while queue:
    now = queue.popleft()
    for nextNode in graph[now]:
        if distance[nextNode] == -1:
            distance[nextNode] = distance[now] + 1
            queue.append(nextNode)

check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True
if check == False:
    print(-1)
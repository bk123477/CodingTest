import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split()) # n:마을/학생 수, m:도로 수, x: 파티 마을
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # (도착점, 시간)

def dijkstra(start): # 개선된 다익스트라 방법
    q = []
    heapq.heappush(q, (0, start)) # (거리, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

ntox = [0] * (n+1) # n마을에서 x마을 거리 저장하는 리스트
xton = [INF] * (n+1) # x마을에서 다른 마을 거리들을 저장하는 리스트
for i in range(1, n+1):
    distance = [INF] * (n+1) # distance 초기화
    dijkstra(i)
    ntox[i] = distance[x] # n마을에서 x마을 가는 거리 저장
    if i == x: xton = distance # x마을일때는 distance 전체 저장
max = 0
for i in range(1, n+1):
    temp = ntox[i] + xton[i]
    if max < temp: max = temp
print(max)
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # n:도시개수
m = int(input()) # m:버스개수
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
dp = [[] for _ in range(n+1)] # 현재단계 까지 오는 최단경로 기록

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 출발, 도착, 비용

s, e = map(int, input().split()) # s:시작, e:끝
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 거리, 노드
    distance[start] = 0
    dp[start].append(start)
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                dp[i[0]] = []
                for path in dp[now]: # 다음 노드의 dp리스트에 지금까지 온 노드들 기록
                    dp[i[0]].append(path)
                dp[i[0]].append(i[0])
dijkstra(s)
print(distance[e])
print(len(dp[e]))
print(' '.join(map(str, dp[e])))
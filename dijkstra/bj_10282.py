import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    n, d, c = map(int, input().split()) # n:컴퓨터개수, d:의존성개수, c:해킹 시작 컴퓨터
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1) # 해킹 하는데 걸리는 시간
    for _ in range(d):
        a, b, s = map(int, input().split()) # b가 감염될 경우 a는 s초 뒤 감염
        graph[b].append((a, s))

    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0 
    li = [c] # 해킹 된 컴퓨터들 번호 저장
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                li.append(i[0])               
                heapq.heappush(q, (cost, i[0]))
    li = set(li) # 중복으로 담기는 원소 제거
    final_node = [] # 해킹 된 컴퓨터들의 distance 저장
    for v in li:
        final_node.append(distance[v])
    print(len(li), max(final_node))

t = int(input())
for _ in range(t):
    dijkstra()
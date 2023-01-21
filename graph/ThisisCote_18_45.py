# acmicpc.net/problem/3665

from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    # 모든 노드에 대해 진입차수 0으로 초기화
    indegree = [0] * (n+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    graph = [[False] * (n+1) for i in range(n+1)]

    # 작년 순위 정보 입력
    data = list(map(int, input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    
    # 올해 변경된 순위 정보 입력
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선의 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    
    # 위상 정렬 시작
    result = []
    q = deque()

    # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    certain = True # 위상 정렬의 결과가 오직 하나인지 판닫ㄴ
    cycle = False

    for i in range(n):
        # 큐가 비어 있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()
import sys
input = sys.stdin.readline
sys.setrecursionlimit(6250000) # RecursionError 방지

def dfs(graph,y,x, n, m):
    if y<0 or x<0 or y>=n or x>=m: # graph 범위 벗어나면 False 리턴
        return False
    if graph[y][x] == 1: # 배추의 상하좌우 탐색
        graph[y][x] = 0 # 방문 처리
        dfs(graph, y-1, x, n, m)
        dfs(graph, y+1, x, n, m)
        dfs(graph, y, x-1, n, m)
        dfs(graph, y, x+1, n, m)
        return True
    return False

t = int(input().rstrip())
result = []
for _ in range(t):
    n, m, k = map(int, input().rstrip().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for _ in range(k): # 배추의 위치를 입력
        yloc, xloc = map(int, input().rstrip().split())
        graph[yloc][xloc] = 1
    for i in range(n):
        for j in range(m):
            if dfs(graph,i,j,n,m):
                count +=1
    result.append(count)
for v in result:
    print(v)
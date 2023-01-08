import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
iceFrame = []
for _ in range(n):
    appendList = []
    tempList = input().rstrip()
    for i in range(len(tempList)):
        appendList.append(int(tempList[i]))
    iceFrame.append(appendList)

def dfs(graph, x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(graph, x-1, y)
        dfs(graph, x+1, y)
        dfs(graph, x, y-1)
        dfs(graph, x, y+1)
    else:
        return

result = 0
for i in range(n):
    for j in range(m):
        if iceFrame[i][j] == 0:
            dfs(iceFrame, i, j)
            result += 1

print(result)
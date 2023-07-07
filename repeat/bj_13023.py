# acmicpc.net/problem/13023

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

friends = [[] for _ in range(N)]
visit = [False] * N
arrive = False

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].apend(a)

def DFS(start, depth):
    global arrive
    visit[start] = True
    if depth == 5:
        arrive = True
        return
    for i in friends[start]:
        if not visit[i]:
            DFS(i, depth+1)
    visit[start] = False

for i in range(N):
    DFS(i, 1)
    if arrive: break

if arrive: print(1)
else: print(0)
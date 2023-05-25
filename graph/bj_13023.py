# acmicpc.net/problem/13023

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# n = 사람의 수, m = 친구 관계의 수
n, m = map(int, input().split())
visit = [False] * n
arrive = False

friends = [[] for _  in range(n)]
for _ in range(m):
    f, s = map(int, input().split())
    friends[f].append(s)
    friends[s].append(f)

def dfs(start, depth):
    global arrive
    visit[start] = True
    if depth==5:
        arrive = True
        return
    for i in friends[start]:
        if visit[i] == False:
            dfs(i, depth+1)
    visit[start] = False

for i in range(n):
    dfs(i, 1)
    if arrive: break

if arrive: print(1)
else: print(0)
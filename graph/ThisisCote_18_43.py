

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * n

roads = []
result = 0
total = 0

for i in range(n):
    parent[i] = i

for _ in range(m):
    x, y, cost = map(int, input().split())
    total += cost
    roads.append((cost, x, y))

roads.sort()

for road in roads:
    cost, x, y = road
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(total-result)
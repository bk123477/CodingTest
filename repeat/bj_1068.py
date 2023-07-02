# acmicpc.net/problem/1068

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(num, info):
    info[num] = -2 # 삭제할 원소
    for i in range(len(info)):
        if num == info[i]: # 방금 삭제한 원소를 부모로 가지고 있는 노드
            dfs(i, info) # 재귀 호출

N = int(input())
info = list(map(int, input().split()))
delete = int(input())

dfs(delete, info)

result = 0
for i in range(N):
    if info[i] != -2 and i not in info:
        result += 1

print(result)
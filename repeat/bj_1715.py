# acmicpc.net/problem/1715

import sys
import heapq
input = sys.stdin.readline

N = int(input())
card_list = []
for _ in range(N):
    card = int(input())
    heapq.heappush(card_list, card)

result = 0
while len(card_list) > 1:
    a = heapq.heappop(card_list)
    b = heapq.heappop(card_list)
    new = a+b
    heapq.heappush(card_list, new)
    result += new

print(result)
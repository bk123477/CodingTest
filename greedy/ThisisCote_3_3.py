import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

cards = []
result = -1

for i in range(n):
    cards.append(list(map(int, input().rstrip().split())))
    cards[i].sort()
    if(result < cards[i][0]):
        result = cards[i][0]

print(result)
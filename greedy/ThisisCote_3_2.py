import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())

li = list(map(int, input().rstrip().split()))
li.sort(reverse=True)

result = 0

first = li[0]
if(k != 1):
    first = li[0] * k + li[1]

result += first * (m//(k+1))
result += li[0] * (m%(k+1))

print(result)
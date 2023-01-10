

import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
aArray = list(map(int, input().rstrip().split()))
bArray = list(map(int, input().rstrip().split()))

aArray.sort()
bArray.sort(reverse=True)

for i in range(k):
    if aArray[i] < bArray[i]:
        aArray[i], bArray[i] = bArray[i], aArray[i]
    else:
        break

result = 0
for number in aArray:
    result += number
print(result)
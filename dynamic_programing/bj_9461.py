import sys

t = int(sys.stdin.readline().rstrip())
result = [1,1,1] + [0] * 97
for i in range(3, 100):
    result[i] = result[i-3] + result[i-2]

for _ in range(t):
    temp = int(sys.stdin.readline().rstrip())
    print(result[temp-1])
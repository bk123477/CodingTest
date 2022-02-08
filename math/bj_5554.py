import sys
input = sys.stdin.readline

re = 0
for _ in range(4):
    re += int(input())

print(re//60)
print(re%60)
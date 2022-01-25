import sys

s = int(sys.stdin.readline().rstrip())
cnt = 1
result = 0
while True:
    result += cnt
    cnt += 1
    if result > s:
        break
print(cnt-2)
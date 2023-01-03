import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

result = 0

while n>1:
    if n == 1: break

    if n % k == 0:
        n //= k
        result += 1
        continue
    else:
        result += (n % k)
        n -= (n % k)
        if n == 0:
            result -= 1
            break

print(result)
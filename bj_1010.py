import sys
def fibo(a, b): # a is start index, b is count
    result = 1
    for i in range(b):
        result *= (a-i)
    return result

t = int(sys.stdin.readline().rstrip())
n, m = [0] * t, [0] * t
for i in range(t):
    n[i], m[i] = map(int, sys.stdin.readline().rstrip().split())

for i in range(t):
    a, b = m[i], n[i]
    if(a-b > b):
        b = a-b
    ja = fibo(a, a-b)
    mo = fibo(a-b, a-b)
    print(int(ja/mo))
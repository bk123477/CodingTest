import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
six = 1001
one = 1001
sum = 0
for i in range(m): # store minimum price
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if(a < six):
        six = a
    if(b < one):
        one = b

# count sum
if(n <= 6):
    print(min(six, n*one))
else:
    if(6*one < six):
        print(n*one)
    else:
        portion = int(n / 6)
        rest = n % 6
        sum = portion * six + min(six, rest*one)
        print(sum)
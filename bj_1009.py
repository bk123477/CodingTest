import sys
two = [6, 2, 4, 8]
three = [1, 3, 9, 7]
seven = [1, 7, 9, 3]

t = int(input())
result = []
for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a %= 10
    if(a == 1 or a == 5 or a == 6):
        result.append(a)
    elif(a == 0):
        result.append(10)
    elif(a == 2 or a == 4 or a == 8):
        if(a == 4):
            b *= 2
        elif(a == 8):
            b *= 3
        result.append(two[b%4])
    elif(a == 3 or a == 9):
        if(a == 9):
            b *= 2
        result.append(three[b%4])
    else:
        result.append(seven[b%4])

for v in result:
    print(v)
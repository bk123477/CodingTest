import sys
n = int(sys.stdin.readline().rstrip())
data = [0] * n
for i in range(n):
    data[i] = int(sys.stdin.readline().rstrip())

data.sort(reverse = True) # sorting

for i in range(n-2):
    if data[i] >= data[i+1] + data[i+2]:
        if i == n-3:
           print(-1)
           break
        else:
            continue
    else:
        print(data[i] + data[i+1] + data[i+2])
        break

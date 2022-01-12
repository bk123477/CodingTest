import sys

data = [[0]*8 for _ in range(8)] #list comprehention

for i in range(8):
    data[i] = sys.stdin.readline().rstrip()

result = 0
for i in range(8):
    if(i%2 == 0):
        for j in range (4):
            if(data[i][2*j] == 'F'):
                result += 1
    else:
        for j in range(4):
            if(data[i][2*j+1] == 'F'):
                result += 1
print(result)
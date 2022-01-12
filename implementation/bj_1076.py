import sys

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
target_multiple = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
third = sys.stdin.readline().rstrip()

result = 0
index = 0
for i in range(10):
    if(color[i] == first):
        result += 10*i
    if(color[i] == second):
        result += i
    if(color[i] == third):
        index = i
print(result * target_multiple[index])
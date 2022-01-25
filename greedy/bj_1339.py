import sys

n = int(sys.stdin.readline().rstrip())
dict1 = {}
for _ in range(n):
    string = sys.stdin.readline().rstrip()
    for i in range(len(string)):
        dict1[string[i]] = dict1.setdefault(string[i], 0) + 10**(len(string) - i-1)
li = []
for k, v in dict1.items():
    li.append((v, k))
li.sort(reverse=True)
result = 0
for i in range(len(li)):
    result += li[i][0] * (9-i)
print(result)
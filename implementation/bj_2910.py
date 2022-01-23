import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
dict1 = {}
li = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(n):
    dict1[li[i]] = dict1.setdefault(li[i], 0) + 1
sorted_dict1 = sorted(dict1.items(), key = lambda x: x[1], reverse=True)
for i in range(len(sorted_dict1)):
    for _ in range(sorted_dict1[i][1]):
        print(sorted_dict1[i][0], end=" ")
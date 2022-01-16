import sys

n = int(sys.stdin.readline().rstrip())
dict1 = {}

for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        dict1[name] = 'enter'
    else:
        dict1.pop(name)
name_list = []
for name in dict1.keys():
    name_list.append(name)
name_list.sort(reverse=True)
for v in name_list:
    print(v)
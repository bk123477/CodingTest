import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
# using python's set data_structure
hear_li = set([sys.stdin.readline().rstrip() for i in range(n)])
see_li = set([sys.stdin.readline().rstrip() for i in range(m)])
result = sorted(list(hear_li & see_li))
print(len(result))
for i in range(len(result)):
    print(result[i])
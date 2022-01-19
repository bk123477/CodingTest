import sys
'''
# using binary_search algorithm
n = int(sys.stdin.readline().rstrip())
a = sorted((map(int, sys.stdin.readline().rstrip().split())))
m = int(sys.stdin.readline().rstrip())
sample = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if target == array[mid]:
        return True
    elif target < array[mid]: # 절반보다 왼쪽에 있음(작은 수)
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for i in sample:
    if binary_search(a, i, 0, n-1):
        print(1)
    else:
        print(0)
'''

# using python's set data_structure
n = int(sys.stdin.readline().rstrip())
array = set(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
sample = list(map(int, sys.stdin.readline().rstrip().split()))

for i in sample:
    if i in array:
        print(1)
    else:
        print(0)
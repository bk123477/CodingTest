

import sys
input = sys.stdin.readline

n = int(input().rstrip())
objectList = list(map(int, input().rstrip().split()))
objectList.sort()
m = int(input().rstrip())
findList = list(map(int, input().rstrip().split()))

def binary_search(objList, findObject, left, right):
    while left <= right:
        mid = (left + right) // 2
        if objList[mid] == findObject:
            return True
        elif objList[mid] > findObject:
            right = mid - 1
        else:
            left = mid + 1
    return False

for findObjects in findList:
    if binary_search(objectList, findObjects, 0, len(objectList)-1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
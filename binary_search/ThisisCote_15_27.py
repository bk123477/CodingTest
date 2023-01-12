# 딕셔너리로 풀었는데 시간초과가 나올지 안나올지 모르겠음..
# 밑에 두 가지 방법 추가
# bisect 부분 자세히 봐 두기.

import sys
from collections import defaultdict
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
numList = list(map(int, input().rstrip().split()))


numDict = defaultdict(lambda: 0)
for num in numList:
    numDict[num] += 1

if numDict[x] == 0:
    print(-1)
else:
    print(numDict[x])



# 첫 번째 방법 이진탐색 구현
def count_by_value(array, x):
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)
    if a == None:
        return 0
    
    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)
    return b - a + 1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid+1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)


# 두 번째 방법 bisect로 풀기
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

count = count_by_range(numList, x, x)
if count == 0: print(-1)
else: print(count)
# acmicpc.net/problem/2108

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
number_list = []
aver = 0
for _ in range(N):
    a = int(input())
    number_list.append(a)
    aver += a
number_list.sort()
print(round(aver/N)) # 산술평균
print(number_list[N // 2]) # 중앙값

dic = defaultdict(int)
for i in range(N):
    dic[number_list[i]] += 1
dic_sort = sorted(dic.items(), key = lambda x:x[1], reverse=True)
if len(dic_sort) == 1:
    print(dic_sort[0][0])
else:
    if dic_sort[0][1] == dic_sort[1][1]:
        print(dic_sort[1][0])
    else:
        print(dic_sort[0][0])

print(number_list[-1] - number_list[0]) # 범위
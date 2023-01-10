# acmicpc.net/problem/10825
# 간단한거였는데 못 풂.. sort key=lambda 쓰는거 확인...

import sys
input = sys.stdin.readline

n = int(input().rstrip())

studentList = []
for _ in range(n):
    name, korean, english, math = input().rstrip().split()
    studentList.append((name, int(korean), int(english), int(math)))

studentList.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in studentList:
    print(student[0])
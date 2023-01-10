# sorted에서 key=lambda 사용하는 방식 기억해두기

import sys
input = sys.stdin.readline

n = int(input().rstrip())
studentList = []
for _ in range(n):
    name, score = input().rstrip().split()
    studentList.append((score, name))

studentList.sort()

# array = sorted(array, key=lambda student: student[1])

for student in studentList:
    print(student[1], end=' ')
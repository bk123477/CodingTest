# acmicpc.net/problem/9251

import sys
input = sys.stdin.readline

first_string = input().rstrip()
second_string = input().rstrip()

cache = [0] * len(second_string)

for i in range(len(first_string)):
    count = 0
    for j in range(len(second_string)):
        if count < cache[j]:
            count = cache[j]
        elif first_string[i] == second_string[j]:
            cache[j] = count + 1

print(max(cache))
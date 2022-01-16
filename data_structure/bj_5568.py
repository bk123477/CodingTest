import sys
from itertools import permutations
# input
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
data = [0] * n
for i in range(n):
    data[i] = int(sys.stdin.readline().rstrip())

permutate = list(permutations(data, k)) # tuple

sum_numbers = {}

for i in range(len(permutate)):
    sum = ''
    for j in range(k):
        sum += str(permutate[i][j])
    sum_numbers[sum] = '1'
result = 0
for v in sum_numbers.keys():
    result += 1
print(result)
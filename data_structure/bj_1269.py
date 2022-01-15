import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
b.sort()
n_a, n_b = 0, 0
a_index, b_index = 0, 0
while True:
    if a_index == n or b_index == m:
        break
    else:
        if a[a_index] < b[b_index]:
            n_a += 1
            a_index += 1
        elif a[a_index] > b[b_index]:
            n_b += 1
            b_index += 1
        else:
            a_index += 1
            b_index += 1
if a[n-1] > b[m-1]:
    n_a += n - a_index
elif a[n-1] < b[m-1]:
    n_b += m - b_index

print(n_a + n_b)

''' # using python's set solution
a, b = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len((A - B)) + len((B - A)))
'''
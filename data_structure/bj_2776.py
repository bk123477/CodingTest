import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    n_list = set(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    m_list = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range(m):
        if m_list[i] in n_list:
            print(1)
        else:
            print(0)
import sys
# 2진수 떠올리기
n, k = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
# 2진수로 바꾼 문자열에서 1의 개수가 k보다 클때
# 해당 되는 자리의 수 만큼 n에 더해줌.
# -> 그러면 1이 점점 오른쪽으로 밀리면서 개수 줄어들음
while bin(n).count('1') > k: 
    # 2진수로 바꾼 문자열의 뒤에서부터 1을 찾음
    l = bin(n)[ : : -1].index('1')
    n += 2 ** l 
    cnt += 2 ** l
print(cnt)
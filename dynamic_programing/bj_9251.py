import sys
input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()

count_table = [[0] * (len(string2)+1) for _ in range(len(string1)+1)] # 2차원 리스트 선언

for i in range(1,len(string1)+1):
    for j in range(1,len(string2)+1):
        if string1[i-1] == string2[j-1]: # 같은 글자 발견된다면
            count_table[i][j] = count_table[i-1][j-1] + 1 # 추가로 발견하기 전 LCS의 최댓값+1을 넣어줌
            continue
        else: # 같은 글자가 아니라면 현재 LCS의 최댓값을 넣어줌
            count_table[i][j] = max(count_table[i-1][j], count_table[i][j-1]) # 이때 max()를 활용해 가장 큰 값을 넣어주어야 함.
            continue

print(count_table[len(string1)][len(string2)])
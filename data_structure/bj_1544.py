import sys

n = int(input())
dict1 = {}
count = 0
for i in range(n): # 단어의 개수만큼 반복
    word_input = sys.stdin.readline().rstrip()
    flag = 0
    for k in dict1.keys(): # dictionary 안에서 단어 검색
        for j in range(len(word_input)): # 단어 돌려가면서 딕셔너리에 있는지 검색
            rotate_word = word_input[j:] + word_input[0:j]
            if k == rotate_word: # 현재 딕셔너리에서 뽑은 단어와 같은 단어 => 더이상 안찾아도됨
                flag = -1
                break
        if flag == -1:
            break  
    # 단어 추가는 여기에서
    if flag == -1:
        continue
    else:
        dict1[word_input] = '1'
for k in dict1.keys():
    count += 1
print(count)
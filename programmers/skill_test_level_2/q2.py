from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    wantDict = defaultdict(lambda: 0)
    
    days = 0
    for i in range(len(want)):
        wantDict[want[i]] = number[i]
        days += number[i]
    for i in range(len(discount)-days+1):
        discountDict = defaultdict(lambda: 0)
        for j in range(days):
            discountDict[discount[i+j]] += 1
        flag = True
        for keys in wantDict.keys():
            if wantDict[keys] != discountDict[keys]:
                flag = False
                break
        if flag:
            answer += 1
  
    return answer

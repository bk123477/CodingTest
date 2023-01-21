def solution(numbers, hand):
    answer = ''
    # numbers는 배열, answer를 LRLL이런식으로 출력 해야함.
    leftPosition = (3, 0)
    rightPosition = (3, 2)
    
    for number in numbers:
        if number % 3 == 1:
            answer += 'L'
            leftPosition = (number//3, 0)
        elif number % 3 == 0 and number > 0:
            answer += 'R'
            rightPosition = (number//3 - 1, 2)
        else:
            leftDistance = rightDistance = 0
            middlePosition = (number//3, 1)
            if number == 0:
                middlePosition = (3, 1)
            
            leftDistance = abs(leftPosition[0] - middlePosition[0]) + abs(leftPosition[1] - middlePosition[1])
            rightDistance = abs(rightPosition[0] - middlePosition[0]) + abs(rightPosition[1] - middlePosition[1])
            if leftDistance > rightDistance:
                rightPosition = middlePosition
                answer += 'R'
            elif leftDistance < rightDistance:
                leftPosition = middlePosition
                answer += 'L'
            else:
                if hand == "right":
                    answer += 'R'
                    rightPosition = middlePosition
                else:
                    answer += 'L'
                    leftPosition = middlePosition
        
    return answer
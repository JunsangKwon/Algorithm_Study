def computeDistance(goal, left, right, hand):
    if(goal == 0):
        goal = 11
    goalLoc = [goal//3, 1]
    leftLoc = [(left-1)//3, (left-1) % 3]
    rightLoc = [(right-1)//3, (right-1) % 3]
    leftDis = abs(leftLoc[0] - goalLoc[0]) + abs(leftLoc[1] - goalLoc[1])
    rightDis = abs(rightLoc[0] - goalLoc[0]) + abs(rightLoc[1] - goalLoc[1])
    if(leftDis > rightDis):
        return 'R'
    elif(leftDis < rightDis):
        return 'L'
    else:
        if(hand == "left"):
            return 'L'
        else:
            return 'R'


def solution(numbers, hand):
    answer = ''
    leftlocation = 10
    rightlocation = 12

    for num in numbers:
        # 규칙 2
        if(num == 1 or num == 4 or num == 7):
            answer += 'L'
            leftlocation = num
        # 규칙 3
        elif(num == 3 or num == 6 or num == 9):
            answer += 'R'
            rightlocation = num
        # 규칙 4
        else:
            tmp = computeDistance(num, leftlocation, rightlocation, hand)
            if(tmp == 'R'):
                if(num == 0):
                    rightlocation = 11
                else:
                    rightlocation = num
            else:
                if(num == 0):
                    leftlocation = 11
                else:
                    leftlocation = num
            answer += tmp

    return answer

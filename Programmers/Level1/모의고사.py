def solution(answers):
    answer = []

    answer1 = []
    answer2 = []
    answer3 = []

    count1 = 1
    count2 = 1

    score1 = 0
    score2 = 0
    score3 = 0

    for i in range(len(answers)):
        # 1번
        if(count1 > 5):
            count1 = 1
        answer1.append(count1)
        count1 += 1

        # 2번
        if(i % 2 == 0):
            answer2.append(2)
        else:
            if(count2 > 5):
                count2 = 1
            answer2.append(count2)
            if(count2 == 1):
                count2 += 2
            else:
                count2 += 1

        # 3번
        if(i % 10 == 0 or i % 10 == 1):
            answer3.append(3)
        elif(i % 10 == 2 or i % 10 == 3):
            answer3.append(1)
        elif(i % 10 == 4 or i % 10 == 5):
            answer3.append(2)
        elif(i % 10 == 6 or i % 10 == 7):
            answer3.append(4)
        else:
            answer3.append(5)

    for i in range(len(answers)):
        if(answers[i] == answer1[i]):
            score1 += 1
        if(answers[i] == answer2[i]):
            score2 += 1
        if(answers[i] == answer3[i]):
            score3 += 1

    maxvalue = max(score1, score2, score3)

    if(maxvalue == score1):
        answer.append(1)
    if(maxvalue == score2):
        answer.append(2)
    if(maxvalue == score3):
        answer.append(3)

    return answer

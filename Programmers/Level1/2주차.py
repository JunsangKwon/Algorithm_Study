def solution(scores):
    answer = ''
    newScoreArray = []
    scoreAverage = []

    for i in range(len(scores)):
        tmpArray = []
        for j in range(len(scores)):
            tmpArray.append(scores[j][i])
        newScoreArray.append(tmpArray)

    for i in range(len(newScoreArray)):
        if (newScoreArray[i][i] == max(newScoreArray[i]) and newScoreArray[i].count(max(newScoreArray[i])) == 1):
            del newScoreArray[i][i]
            continue

        if (newScoreArray[i][i] == min(newScoreArray[i]) and newScoreArray[i].count(min(newScoreArray[i])) == 1):
            del newScoreArray[i][i]
            continue

    for i in range(len(newScoreArray)):
        scoreAverage.append(sum(newScoreArray[i])/len(newScoreArray[i]))

    for avg in scoreAverage:
        if(avg >= 90):
            answer += 'A'
        elif(avg >= 80 and avg < 90):
            answer += 'B'
        elif(avg >= 70 and avg < 80):
            answer += 'C'
        elif(avg >= 50 and avg < 70):
            answer += 'D'
        else:
            answer += 'F'

    return answer

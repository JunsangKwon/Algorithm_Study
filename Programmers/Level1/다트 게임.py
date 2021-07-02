def solution(dartResult):
    answer = 0
    scoreList = []
    word = ''
    for i in range(len(dartResult)):
        if(dartResult[i] == "*" or dartResult[i] == "#"):
            word += dartResult[i]
            scoreList.append(word)
            word = ''
            continue
        elif(dartResult[i] == "S" or dartResult[i] == "D" or dartResult[i] == "T"):
            if(i != len(dartResult)-1 and (dartResult[i+1] == "*" or dartResult[i+1] == "#")):
                word += dartResult[i]
                continue
            else:
                word += dartResult[i]
                scoreList.append(word)
                word = ''
        else:
            word += dartResult[i]

    results = []
    index = 0
    for score in scoreList:
        exp = 1
        if(score[0] == '1' and score[1] == '0'):
            if(score[2] == "D"):
                exp = 2
            elif(score[2] == "T"):
                exp = 3
            result = 10 ** exp
        else:
            if(score[1] == "D"):
                exp = 2
            elif(score[1] == "T"):
                exp = 3
            result = int(score[0]) ** exp
        if(len(score) == 3):
            if(score[2] == "*"):
                if(index != 0):
                    results[-1] = results[-1]*2
                result = result*2
            elif(score[2] == "#"):
                result = result*(-1)
            results.append(result)
            index += 1
        elif(len(score) == 4):
            if(score[3] == "*"):
                if(index != 0):
                    results[-1] = results[-1]*2
                result = result*2
            else:
                result = result*(-1)
            results.append(result)
            index += 1
        else:
            results.append(result)
            index += 1

    return sum(results)

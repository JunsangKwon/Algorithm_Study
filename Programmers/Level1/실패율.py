def solution(N, stages):
    answer = []
    defeatRate = []

    for stage in range(1, N+1):
        denominator = 0
        numerator = 0
        for user in stages:
            if(stage <= user):
                denominator += 1
            if(stage == user):
                numerator += 1

        if(denominator == 0):
            defeatRate.append((0, stage))
        else:
            value = numerator/denominator
            defeatRate.append((value, stage))

    defeatRate = sorted(defeatRate, key=lambda x: (-x[0], x[1]))
    for i in range(len(defeatRate)):
        answer.append(defeatRate[i][1])

    return answer

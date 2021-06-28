def solution(d, budget):
    answer = 0
    sumOfD = 0
    d.sort()
    for i in range(len(d)):
        sumOfD += d[i]
        if(sumOfD > budget):
            answer = i
            break
        else:
            answer = i+1

    return answer

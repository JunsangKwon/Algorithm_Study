def solution(progresses, speeds):
    answer = []
    count = [0]*len(speeds)

    for i in range(len(speeds)):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count[i] += 1

    tmp = count[0]
    func = 1
    index = 0
    isFinished = False
    for c in count:
        if(index == 0):
            index += 1
            continue
        if(tmp < c):
            answer.append(func)
            func = 1
            tmp = c
            index += 1
        else:
            func += 1
            index += 1

    answer.append(func)

    return answer

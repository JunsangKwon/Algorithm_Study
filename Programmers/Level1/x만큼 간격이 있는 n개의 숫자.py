def solution(x, n):
    answer = []
    originX = x
    for i in range(n):
        if(i == 0):
            answer.append(x)
            continue
        x += originX
        answer.append(x)

    return answer

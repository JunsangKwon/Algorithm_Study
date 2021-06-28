def solution(n):
    answer = 0
    numstr = str(n)
    for i in range(len(numstr)):
        answer += int(numstr[i])

    return answer

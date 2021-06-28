def solution(n):
    answer = 0
    isFind = False
    for i in range(n+1):
        if(i*i == n):
            isFind = True
            answer = (i+1) ** 2
            break

    if(not isFind):
        return -1

    return answer

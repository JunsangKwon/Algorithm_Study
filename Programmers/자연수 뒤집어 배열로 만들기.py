def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)):
        answer.append(n[i])
    answer.reverse()
    for i in range(len(answer)):
        answer[i] = int(answer[i])

    return answer

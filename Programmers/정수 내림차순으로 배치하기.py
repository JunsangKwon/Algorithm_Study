def solution(n):
    answer = ''
    n = str(n)
    n = sorted(n, reverse=True)
    for s in n:
        answer += s
    answer = int(answer)
    return answer

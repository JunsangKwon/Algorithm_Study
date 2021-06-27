def solution(n):
    watermelon = ['수', '박'] * 5001
    answer = ''
    for i in range(n):
        answer += watermelon[i]

    return answer

def solution(n):
    answer = 0
    remainder = []
    while(n >= 3):
        remainder.append(n % 3)
        n //= 3
    remainder.append(n)
    remainder.reverse()

    for i in range(len(remainder)):
        answer += remainder[i] * (3 ** i)

    return answer

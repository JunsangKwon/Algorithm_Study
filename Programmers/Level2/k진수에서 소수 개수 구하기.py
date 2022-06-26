import math


def change_10_to_n(n, value):
    result = ''
    q, r = divmod(n, value)
    while q > 0:
        result += str(r)
        q, r = divmod(q, value)

    result += str(r)

    return result[::-1]


def solution(n, k):
    answer = 0
    num = change_10_to_n(n, k)

    candidate = num.split('0')

    for i in range(len(candidate)):
        is_prime = True
        if candidate[i] == '' or candidate[i] == '1':
            continue
        candidate_num = int(candidate[i])

        for j in range(2, int(math.sqrt(candidate_num)) + 1):
            if candidate_num % j == 0:
                is_prime = False
                break

        if is_prime:
            answer += 1
            print(candidate_num)

    return answer

def solution(n):
    piv = [0, 1]
    for i in range(2, n+1):
        piv.append(piv[i-1] + piv[i-2])
    answer = piv[n] % 1234567
    return answer

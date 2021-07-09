def solution(n, m):
    answer = []
    divisorN = []
    divisorM = []
    commonDivisor = []

    for i in range(1, min(n, m)+1):
        if(n % i == 0):
            divisorN.append(i)
        if(m % i == 0):
            divisorM.append(i)

    for i in divisorN:
        if(i in divisorM):
            commonDivisor.append(i)

    maxDivisor = max(commonDivisor)
    minMultiple = maxDivisor * (n//maxDivisor) * (m//maxDivisor)
    answer.append(maxDivisor)
    answer.append(minMultiple)

    return answer

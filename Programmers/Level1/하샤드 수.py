def solution(x):
    answer = True
    strNum = str(x)
    sumOfDigits = 0
    for i in range(len(strNum)):
        sumOfDigits += int(strNum[i])
    if(x % sumOfDigits != 0):
        answer = False

    return answer

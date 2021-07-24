def solution(n):
    answer = ''
    numbers = []
    while(n >= 3):
        div = n % 3
        if(div == 1):
            numbers.append('1')
            n //= 3
        elif(div == 2):
            numbers.append('2')
            n //= 3
        else:
            numbers.append('4')
            n = n//3 - 1
    if(n != 0):
        numbers.append(str(n))
    numbers.reverse()

    for n in numbers:
        answer += n

    return answer

def solution(s):
    answer = ''
    minusFlag = False
    numbers = []
    tmp = ''
    for i in range(len(s)):
        if(i == len(s)-1):
            tmp += ('%s' % s[i])
            value = int(tmp)
            if(minusFlag):
                value = -1 * value
                minusFlag = False
            numbers.append(value)
            tmp = ''
            break
        if(s[i] == " "):
            continue
        elif(s[i] == "-"):
            minusFlag = True
        elif(s[i+1] != " "):
            tmp += ('%s' % s[i])
        else:
            tmp += ('%s' % s[i])
            value = int(tmp)
            if(minusFlag):
                value = -1 * value
                minusFlag = False
            numbers.append(value)
            tmp = ''

    print(numbers)
    answer += ('%s' % min(numbers))
    answer += " "
    answer += ('%s' % max(numbers))

    return answer

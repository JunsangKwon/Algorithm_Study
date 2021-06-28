def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if(s[i] == ' '):
            answer += ' '
            continue
        tmp = ord(s[i]) + n
        if(ord(s[i]) <= 122 and tmp > 122):
            tmp -= 26
        elif(ord(s[i]) <= 90 and tmp > 90):
            tmp -= 26
        answer += chr(tmp)

    return answer

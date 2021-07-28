def solution(s):
    is_first = True
    answer = ''
    for i in range(len(s)):
        if(is_first):
            if(s[i] == " "):
                is_first = True
                answer += " "
                continue
            answer += s[i].upper()
            is_first = False
        else:
            if(s[i] == " "):
                is_first = True
                answer += " "
            else:
                answer += s[i].lower()

    return answer

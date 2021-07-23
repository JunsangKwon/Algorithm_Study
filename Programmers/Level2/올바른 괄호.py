def solution(s):
    answer = True
    bracket_arr = []

    for i in range(len(s)):
        if(s[i] == '('):
            bracket_arr.append(s[i])
        else:
            if(len(bracket_arr) == 0):
                answer = False
                break
            else:
                bracket_arr.pop(-1)

    if(len(bracket_arr) != 0):
        answer = False

    return answer

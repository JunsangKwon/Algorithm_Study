def solution(s):
    index = 0
    word = ''
    for i in range(len(s)):
        if(s[i] != ' ' and index % 2 == 0):
            word += s[i].upper()
            index += 1
        elif(s[i] != ' ' and index % 2 == 1):
            word += s[i].lower()
            index += 1
        else:
            word += ' '
            index = 0

    return word

def solution(s):
    s = s.lower()
    pnum = ynum = 0

    for i in range(len(s)):
        if(s[i] == 'p'):
            pnum += 1
        elif(s[i] == 'y'):
            ynum += 1

    return pnum == ynum

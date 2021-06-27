def solution(n, lost, reserve):
    count = 0
    canparticipate = [False]*len(lost)
    for i in range(len(lost)):
        for j in reserve:
            if lost[i] == j:
                canparticipate[i] = True
                reserve.remove(j)
                break

    for i in range(len(lost)):
        for j in reserve:
            if(canparticipate[i]):
                continue
            if(lost[i] - 1 == j or lost[i]+1 == j):
                canparticipate[i] = True
                reserve.remove(j)
                break

    for b in canparticipate:
        if(b == False):
            count += 1

    return n - count

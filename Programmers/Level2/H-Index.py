def solution(citations):
    h_index = 0

    for i in range(0, max(citations)):
        count = 0
        for j in citations:
            if(i <= j):
                count += 1
        if(count >= i and h_index < i):
            h_index = i

    return h_index

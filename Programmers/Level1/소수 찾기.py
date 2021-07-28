def solution(n):
    arr = [0, 0]
    answer = 0

    for i in range(2, n+1):
        arr.append(i)

    for i in range(2, n+1):
        if(arr[i] == 0):
            continue

        for j in range(i*2, n+1, i):
            arr[j] = 0

    for i in range(2, n+1):
        if(arr[i] != 0):
            answer += 1

    return answer

def solution(arr1, arr2):
    row = len(arr1[0])
    col = len(arr1)
    answer = arr1

    for i in range(col):
        for j in range(row):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

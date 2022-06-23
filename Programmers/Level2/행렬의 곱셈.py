def solution(arr1, arr2):
    answer = []
    arr2 = list(map(list, zip(*arr2)))

    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2)):
            total = 0
            for k in range(len(arr1[i])):
                total += arr1[i][k] * arr2[j][k]
            row.append(total)
        answer.append(row)

    return answer

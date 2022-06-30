def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []

    for i in range(len(arr1)):
        code = format(arr1[i], 'b')
        while len(code) < n:
            code = '0' + code
        map1.append(code)

    for i in range(len(arr2)):
        code = format(arr2[i], 'b')
        while len(code) < n:
            code = '0' + code
        map2.append(code)

    for i in range(n):
        tmp = ''
        for j in range(n):
            if map1[i][j] == map2[i][j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)

    return answer

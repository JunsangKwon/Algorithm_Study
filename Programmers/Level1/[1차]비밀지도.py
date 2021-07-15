def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    real_map = []

    for i in range(n):
        value1 = format(arr1[i], 'b')
        value2 = format(arr2[i], 'b')

        if(len(value1) < n):
            dif = n - len(value1)
            value1 = '0' * dif + value1
        if(len(value2) < n):
            dif = n - len(value2)
            value2 = '0' * dif + value2
        map1.append(value1)
        map2.append(value2)

    for i in range(n):
        value = ''
        for j in range(n):
            if(map1[i][j] == '1' or map2[i][j] == '1'):
                value += '1'
            else:
                value += '0'
        real_map.append(value)

    for rm in real_map:
        rm = rm.replace('1', '#')
        rm = rm.replace('0', ' ')
        answer.append(rm)

    return answer

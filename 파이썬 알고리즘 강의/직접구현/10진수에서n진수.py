n_dic1 = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}

n_dic2 = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


def change_10_to_n(n, value):
    result = ''
    q, r = divmod(n, value)
    while q > 0:
        result += n_dic1[r]
        q, r = divmod(q, value)

    result += n_dic1[r]

    return result[::-1]


def change_n_to_10(s, value):
    result = 0
    s = s[::-1]
    for i in range(len(s)):
        result += n_dic2[s[i]] * (value ** i)

    return result


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_board = list(map(list, zip(*board)))
print(new_board)

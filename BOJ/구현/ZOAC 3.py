lw, rw = map(str, input().split())
target = input()
left_keyboard = [['q', 'w', 'e', 'r', 't'], [
    'a', 's', 'd', 'f', 'g'], ['z', 'x', 'c', 'v']]
right_keyboard = [['0', 'y', 'u', 'i', 'o', 'p'], [
    '0', 'h', 'j', 'k', 'l'], ['b', 'n', 'm']]
left_words = 'qwertasdfgzxcv'
right_words = 'yuiophjklbnm'

isLeft = False
time = 0


def find_coordinate(s, isLeft):
    break_flag = False
    coor_i = 0
    coor_j = 0

    if isLeft:
        for i in range(len(left_keyboard)):
            for j in range(len(left_keyboard[i])):
                if s == left_keyboard[i][j]:
                    coor_i = i
                    coor_j = j
                    break_flag = True
                    break
            if break_flag:
                break_flag = False
                break
    else:
        for i in range(len(right_keyboard)):
            for j in range(len(right_keyboard[i])):
                if s == right_keyboard[i][j]:
                    coor_i = i
                    coor_j = j
                    break_flag = True
                    break
            if break_flag:
                break_flag = False
                break
    return (coor_i, coor_j)


left_prev_coor = find_coordinate(lw, True)
right_prev_coor = find_coordinate(rw, False)

for i in range(len(target)):
    if target[i] in left_words:
        isLeft = True
    else:
        isLeft = False

    if isLeft:
        coor = find_coordinate(target[i], True)
        time += (abs(coor[0] - left_prev_coor[0]) +
                 abs(coor[1] - left_prev_coor[1]) + 1)
        left_prev_coor = coor
    else:
        coor = find_coordinate(target[i], False)
        time += (abs(coor[0] - right_prev_coor[0]) +
                 abs(coor[1] - right_prev_coor[1]) + 1)
        right_prev_coor = coor

print(time)

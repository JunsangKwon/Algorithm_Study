def solution(sizes):
    answer = 0
    rotate_sizes = list(map(list, zip(*sizes)))

    max_width = max(rotate_sizes[0])
    max_height = max(rotate_sizes[1])

    if max_width >= max_height:
        while True:
            change_flag = False
            for i in range(len(rotate_sizes[1])):
                if rotate_sizes[1][i] == max_height and rotate_sizes[1][i] > rotate_sizes[0][i]:
                    rotate_sizes[1][i], rotate_sizes[0][i] = rotate_sizes[0][i], rotate_sizes[1][i]
                    change_flag = True

            max_height = max(rotate_sizes[1])

            if not change_flag:
                break
        answer = max_width * max_height

    elif max_width < max_height:
        while True:
            change_flag = False
            for i in range(len(rotate_sizes[0])):
                if rotate_sizes[0][i] == max_width and rotate_sizes[0][i] > rotate_sizes[1][i]:
                    rotate_sizes[0][i], rotate_sizes[1][i] = rotate_sizes[1][i], rotate_sizes[0][i]
                    change_flag = True

            max_width = max(rotate_sizes[0])

            if not change_flag:
                break
        answer = max_width * max_height

    return answer

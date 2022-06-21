def solution(numbers, hand):
    result = ''
    key_pad = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [
        1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}
    left_finger = [3, 0]
    right_finger = [3, 2]
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            left_finger = key_pad[numbers[i]]
            result += 'L'
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            right_finger = key_pad[numbers[i]]
            result += 'R'
        else:
            target_coor = key_pad[numbers[i]]
            left_distance = abs(
                target_coor[0] - left_finger[0]) + abs(target_coor[1] - left_finger[1])
            right_distance = abs(
                target_coor[0] - right_finger[0]) + abs(target_coor[1] - right_finger[1])
            if left_distance > right_distance:
                right_finger = key_pad[numbers[i]]
                result += 'R'
            elif left_distance < right_distance:
                left_finger = key_pad[numbers[i]]
                result += 'L'
            else:
                if hand == 'right':
                    right_finger = key_pad[numbers[i]]
                    result += 'R'
                else:
                    left_finger = key_pad[numbers[i]]
                    result += 'L'

    return result

from sys import stdin
from collections import deque

input = stdin.readline

answer_arr_list = []
deq = deque()


def rotate_array(arr, count):
    new_arr = arr
    n = len(arr)
    main_diag = []
    sub_diag = []
    center_col = []
    center_row = []
    for i in range(n):
        main_diag.append(arr[i][i])
        center_col.append(arr[i][n // 2])
        sub_diag.append(arr[i][n-i-1])
        center_row.append(arr[n // 2][i])
    deq.append(main_diag)
    deq.append(center_col)
    deq.append(sub_diag)
    deq.append(center_row)
    if count >= 0:
        for i in range(count):
            deq.rotate()
            tmp = deq.pop()
            tmp.reverse()
            deq.append(tmp)
    else:
        for i in range(abs(count)):
            tmp = deq.pop()
            tmp.reverse()
            deq.append(tmp)
            deq.rotate(-1)

    for i in range(4):
        tmp_arr = deq.popleft()
        for j in range(n):
            if i == 0:
                new_arr[j][j] = tmp_arr[j]
            elif i == 1:
                new_arr[j][n // 2] = tmp_arr[j]
            elif i == 2:
                new_arr[j][n-j-1] = tmp_arr[j]
            else:
                new_arr[n // 2][j] = tmp_arr[j]

    for i in range(n):
        answer_arr_list.append(new_arr[i])


for _ in range(int(input())):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rotate_array(arr, d // 45)

for i in range(len(answer_arr_list)):
    for j in range(len(answer_arr_list[i])):
        print(answer_arr_list[i][j], end=" ")
    print()

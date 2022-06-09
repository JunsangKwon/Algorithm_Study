N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
move = [N, M, N, M]
result_arr = arr

n = min(N, M) // 2


def rotate_arr(starti, startj, arr, count):
    ci = arr[starti][startj]


for i in range(n):
    starti = i
    startj = i
    rotate_arr(starti, startj, arr, R)

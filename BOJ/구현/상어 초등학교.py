n = int(input())
best_friends = {}
classroom = [[-1] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
orders = []
answer = 0


def search(ci, cj, s_id):
    count = 0
    blank_count = 0
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for i in range(4):
        ki = ci + di[i]
        kj = cj + dj[i]
        if ki < 0 or kj < 0 or ki >= n or kj >= n:
            continue
        if classroom[ki][kj] in best_friends[s_id]:
            count += 1
        elif classroom[ki][kj] == -1:
            blank_count += 1

    return [ci, cj, count, blank_count]


def happy(ci, cj, s_id):
    count = 0
    total = 0
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for i in range(4):
        ki = ci + di[i]
        kj = cj + dj[i]
        if ki < 0 or kj < 0 or ki >= n or kj >= n:
            continue
        if classroom[ki][kj] in best_friends[s_id]:
            count += 1

    if count == 1:
        total += 1
    elif count == 2:
        total += 10
    elif count == 3:
        total += 100
    elif count == 4:
        total += 1000

    return total


for i in range(n ** 2):
    student_id, *arr = map(int, input().split())
    best_friends[student_id] = arr
    orders.append(student_id)

for s_id in orders:
    count_list = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and classroom[i][j] == -1:
                count_list.append(search(i, j, s_id))

    count_list.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))

    classroom[count_list[0][0]][count_list[0][1]] = s_id
    visited[count_list[0][0]][count_list[0][1]] = True
    count_list.clear()

for i in range(n):
    for j in range(n):
        answer += happy(i, j, classroom[i][j])

print(answer)

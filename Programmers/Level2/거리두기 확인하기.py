from collections import deque


def find(ci, cj, place, visited):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    q = deque()
    visited[ci][cj] = True
    q.append([ci, cj, 0])
    break_flag = False

    while q:
        tmpi = q[0][0]
        tmpj = q[0][1]
        depth = q[0][2]
        if break_flag or depth >= 2:
            break
        q.popleft()

        for i in range(4):
            ki = tmpi + di[i]
            kj = tmpj + dj[i]
            kdepth = depth + 1
            if ki < 0 or ki >= 5 or kj < 0 or kj >= 5 or visited[ki][kj] or place[ki][kj] == 'X':
                continue
            if place[ki][kj] == 'P':
                break_flag = True
                break
            else:
                q.append([ki, kj, kdepth])
                visited[ki][kj] = True

    if break_flag:
        return False
    else:
        return True


def solution(places):
    answer = []

    for x in range(5):
        flag = False
        place = places[x]
        visited = [[False] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not find(i, j, place, visited):
                        flag = True
                        break
            if flag:
                break

        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer

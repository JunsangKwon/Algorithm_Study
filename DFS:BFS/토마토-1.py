from collections import deque

# 문제점 : 지금 하나씩 들어가서, 그게 끝날때까지 계속 되는거라, 나머지 하나는 아예 진행이 안됨


def bfs(farm, visited):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    q = deque()
    maxDay = 0
    flag = False
    flag2 = False

    for i in range(n):
        if(flag):
            break
        for j in range(m):
            if(farm[i][j] == 0):
                flag = True
                break

    if(not flag):
        print(0)
        return

    for i in range(n):
        for j in range(m):
            if(farm[i][j] == 0 or farm[i][j] == -1 or visited[i][j]):
                continue
            tmp = (i, j, 0)
            visited[i][j] = True
            q.append(tmp)

    while(q):
        ti = q[0][0]
        tj = q[0][1]
        tday = q[0][2]
        q.popleft()
        for k in range(4):
            ki = ti + di[k]
            kj = tj + dj[k]
            kday = tday + 1
            if(ki < 0 or kj < 0 or ki >= n or kj >= m or farm[ki][kj] == 1 or visited[ki][kj] or farm[ki][kj] == -1):
                continue
            farm[ki][kj] = 1
            visited[ki][kj] = True
            tmplist = [ki, kj, kday]
            if maxDay < kday:
                maxDay = kday
            q.append(tuple(tmplist))

    for i in range(n):
        if(flag2):
            break
        for j in range(m):
            if(farm[i][j] == 0):
                flag2 = True
                break

    if(flag2):
        print(-1)
        return

    print(maxDay)


m, n = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
bfs(farm, visited)

from collections import deque


def bfs(maze, visited):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    q = deque()

    start = (0, 0, 1)
    q.append(start)
    visited[0][0] = True

    while(q):
        ti = q[0][0]
        tj = q[0][1]
        tdepth = q[0][2]
        if(ti == n-1 and tj == m-1):
            print(tdepth)
            break
        q.popleft()

        for k in range(4):
            ki = ti + di[k]
            kj = tj + dj[k]
            kdepth = tdepth + 1
            if(ki < 0 or ki >= n or kj < 0 or kj >= m or maze[ki][kj] == 0 or visited[ki][kj]):
                continue

            tmplist = []
            tmplist.append(ki)
            tmplist.append(kj)
            tmplist.append(kdepth)
            q.append(tuple(tmplist))
            visited[ki][kj] = True


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
bfs(maze, visited)

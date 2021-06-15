from collections import deque

'''
5 5
00000
11101
00001
01111
00010
'''


def bfs(maze, visited):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    q = deque()
    flag = False

    start = (0, 0, 1, 0)
    q.append(start)
    visited[0][0] = True

    while(q):
        ti = q[0][0]
        tj = q[0][1]
        tdepth = q[0][2]
        bc = q[0][3]
        if(ti == n-1 and tj == m-1):
            print(tdepth)
            flag = True
            break
        q.popleft()

        for k in range(4):
            ki = ti + di[k]
            kj = tj + dj[k]
            kdepth = tdepth + 1
            kbc = bc
            if(ki < 0 or ki >= n or kj < 0 or kj >= m or visited[ki][kj]):
                continue

            if(maze[ki][kj] == 1):
                if(kbc == 0):
                    kbc += 1
                else:
                    continue

            q.append((ki, kj, kdepth, kbc))
            visited[ki][kj] = True

    if(not flag):
        print(-1)


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
bfs(maze, visited)

from collections import deque

T = int(input())
answers = []


def bfs(land, visited):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    q = deque()
    count = 0

    for i in range(n):
        for j in range(m):
            if(land[i][j] == 0 or visited[i][j]):
                continue
            tmplist = []
            tmplist.append(i)
            tmplist.append(j)
            q.append(tuple(tmplist))
            count += 1
            visited[i][j] = True

            while(q):
                ti = q[0][0]
                tj = q[0][1]
                q.popleft()

                for k in range(4):
                    ki = ti + di[k]
                    kj = tj + dj[k]
                    if(ki < 0 or ki >= n or kj < 0 or kj >= m or land[ki][kj] == 0 or visited[ki][kj]):
                        continue

                    tmplist = []
                    tmplist.append(ki)
                    tmplist.append(kj)
                    q.append(tuple(tmplist))
                    visited[ki][kj] = True

    answers.append(count)


for _ in range(T):
    m, n, k = map(int, input().split())
    land = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        land[y][x] = 1

    bfs(land, visited)

for l in answers:
    print(l)

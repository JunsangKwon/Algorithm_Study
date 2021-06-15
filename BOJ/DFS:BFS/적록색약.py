from collections import deque


def bfs(pic, visited):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    q = deque()
    count = 0

    for i in range(n):
        for j in range(n):
            if(visited[i][j]):
                continue
            q.append([i, j, pic[i][j]])
            visited[i][j] = True
            count += 1

            while(q):
                ti = q[0][0]
                tj = q[0][1]
                tc = q[0][2]
                q.popleft()

                for k in range(4):
                    ki = ti + di[k]
                    kj = tj + dj[k]
                    if(ki < 0 or ki >= n or kj < 0 or kj >= n or pic[ki][kj] != tc or visited[ki][kj]):
                        continue

                    q.append([ki, kj, tc])
                    visited[ki][kj] = True

    answers.append(count)


n = int(input())
answers = []

pic1 = [list(map(str, input())) for _ in range(n)]
pic2 = [["C"] * n for _ in range(n)]


for i in range(n):
    for j in range(n):
        if pic1[i][j] == "G":
            pic2[i][j] = "R"
        else:
            pic2[i][j] = pic1[i][j]


visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

bfs(pic1, visited1)
bfs(pic2, visited2)

print("%d %d" % (answers[0], answers[1]))

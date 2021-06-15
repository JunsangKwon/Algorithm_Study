from collections import deque


def bfs(visited):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    q = deque()

    for i in range(n):
        for j in range(n):
            if(dangee[i][j] == 0 or visited[i][j] == True):
                continue
            tmplist = []
            tmplist.append(i)
            tmplist.append(j)
            q.append(tuple(tmplist))
            visited[i][j] = True
            count = 0
            while(q):
                ti = q[0][0]
                tj = q[0][1]
                q.popleft()
                count += 1

                for k in range(4):
                    ki = ti + di[k]
                    kj = tj + dj[k]
                    if(ki >= 0 and ki < n and kj >= 0 and kj < n and dangee[ki][kj] == 1 and visited[ki][kj] == False):
                        tmplist = []
                        tmplist.append(ki)
                        tmplist.append(kj)
                        q.append(tuple(tmplist))
                        visited[ki][kj] = True
            answers.append(count)


n = int(input())
answers = []
dangee = [list(map(int, input())) for _ in range(n)]  # 2차원 배열 입력받는 법
visited = [[False] * n for _ in range(n)]
bfs(visited)

print(len(answers))
answers.sort()
for i in answers:
    print(i)

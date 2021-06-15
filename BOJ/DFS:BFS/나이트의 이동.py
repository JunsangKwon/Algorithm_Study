from collections import deque


def bfs(chess, visited, si, sj):
    q = deque()
    mi = [-2, -1, 1, 2, 2, 1, -1, -2]
    mj = [1, 2, 2, 1, -1, -2, -2, -1]

    visited[si][sj] = True
    q.append((si, sj, 0))
    while(q):
        ti = q[0][0]
        tj = q[0][1]
        tcount = q[0][2]
        q.popleft()
        for i in range(8):
            ki = ti + mi[i]
            kj = tj + mj[i]
            kcount = tcount + 1
            if(ki < 0 or ki >= l or kj < 0 or kj >= l or visited[ki][kj]):
                continue
            if chess[ki][kj] == 1:
                answers.append(kcount)
                q.clear()
                break
            q.append((ki, kj, kcount))
            visited[ki][kj] = True


testcase = int(input())
answers = []

for _ in range(testcase):
    l = int(input())
    flag = False
    si, sj = map(int, input().split())
    di, dj = map(int, input().split())
    chess = [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]
    chess[di][dj] = 1
    if(si == di and sj == dj):
        flag = True
        answers.append(0)
    if(not flag):
        bfs(chess, visited, si, sj)

for i in answers:
    print(i)

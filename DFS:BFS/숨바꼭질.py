from collections import deque


def bfs(road, n, visited):

    q = deque()
    start = (n, 0)
    q.append(start)
    while(q):
        ti = q[0][0]
        ttime = q[0][1]
        q.popleft()
        for i in range(3):
            if i == 0:
                if (ti+1 > 100000 or visited[ti+1]):
                    continue
                if road[ti+1] == 1:
                    print(ttime+1)
                    return
                else:
                    visited[ti+1] = True
                    q.append((ti+1, ttime+1))
            elif i == 1:
                if (ti-1 < 0 or visited[ti-1]):
                    continue
                if road[ti-1] == 1:
                    print(ttime+1)
                    return
                else:
                    visited[ti-1] = True
                    q.append((ti-1, ttime+1))
            else:
                if (2*ti > 100000 or visited[2*ti]):
                    continue
                if road[2*ti] == 1:
                    print(ttime+1)
                    return
                else:
                    visited[2*ti] = True
                    q.append((2*ti, ttime+1))


road = [0] * 100001
visited = [False] * 100001
n, k = map(int, input().split())
flag = False
road[n] = 1
road[k] = 1
visited[n] = True
if(n == k):
    flag = True

if(flag):
    print(0)

bfs(road, n, visited)

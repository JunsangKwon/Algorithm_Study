from collections import deque


def bfs(graph, start, visited):
    count = 0
    q = deque([start])
    visited[start] = True

    while(q):
        v = q.popleft()
        # pop 할 때마다 1씩 더해줌
        count += 1
        for i in graph[v]:
            if(not visited[i]):
                q.append(i)
                visited[i] = True

    # 1을 pop하는 경우는 제외한다 => -1 해줌
    return count-1


n = int(input())
m = int(input())

graph = [[]*n for i in range(n+1)]
for i in range(m):
    tmp1, tmp2 = map(int, input().split())
    graph[tmp1].append(tmp2)
    graph[tmp2].append(tmp1)

visited = [False]*(n+1)

print(graph)
print(bfs(graph, 1, visited))

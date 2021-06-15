from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    # 작은 순서대로 출력하기 위해 정렬
    graph[v].sort()
    for i in graph[v]:
        if(not visited[i]):
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while(queue):
        v = queue.popleft()
        print(v, end=" ")

        # 작은 순서대로 출력하기 위해 정렬
        graph[v].sort()
        for i in graph[v]:
            if(not visited[i]):
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]

# 인접 리스트로 구현한 Graph
for i in range(m):
    tmp1, tmp2 = map(int, input().split())
    graph[tmp1].append(tmp2)
    graph[tmp2].append(tmp1)

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)

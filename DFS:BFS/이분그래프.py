from collections import deque


def bfs(graph, visited):
    q = deque()
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


tc = int(input())
answers = []

for t in range(tc):
    v, e = map(int, input().split())
    matrix = [[0]*v for i in range(v)]

    for vc in range(v):
        i, j = map(int, input().split())
        matrix[i].append(j)
        matrix[j].append(i)

    visited = [False]*(n+1)
    bfs(matrix, visited)

for a in answers {
    print(a)
}

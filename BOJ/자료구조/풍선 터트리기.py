from collections import deque

n = int(input())
papers = list(map(int, input().split()))
q = deque()
answer = []

for i in range(len(papers)):
    q.append([papers[i], i+1])

while q:
    print(q)
    paper = q[0][0]
    answer.append(q[0][1])
    q.popleft()
    if paper > 0:
        q.rotate(-1 * paper + 1)
    else:
        q.rotate(-1 * paper)

for a in answer:
    print(a, end=" ")

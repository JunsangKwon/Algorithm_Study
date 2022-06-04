from collections import Counter

answer = []

while True:
    N, M = map(int, input().split())
    arr = []
    seconds = []
    if N == M == 0:
        break

    for i in range(N):
        arr += list(map(int, input().split()))

    val = Counter(arr).most_common()

    for v in val:
        if v[1] == val[1][1]:
            seconds.append(v[0])

    seconds.sort()
    answer.append(seconds)

for i in range(len(answer)):
    for j in range(len(answer[i])):
        print(answer[i][j], end=" ")
    print()

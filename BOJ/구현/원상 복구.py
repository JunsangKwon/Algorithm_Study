n, k = map(int, input().split())

s = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(k):
    tmp = [0] * n
    for i in range(n):
        tmp[d[i] - 1] = s[i]
    s = tmp


for i in range(n):
    print(s[i], end=" ")

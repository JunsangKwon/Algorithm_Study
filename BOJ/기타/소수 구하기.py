from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [0] * (m+1)

for i in range(2, m+1):
    arr[i] = i

for i in range(2, m+1):
    if(arr[i] == 0):
        continue

    for j in range(i*2, m+1, i):
        arr[j] = 0

for i in range(n, m+1):
    if(arr[i] != 0):
        print(arr[i])

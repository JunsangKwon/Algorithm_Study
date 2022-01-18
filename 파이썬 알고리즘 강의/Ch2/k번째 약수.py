from sys import stdin

input = stdin.readline

n, k = map(int, stdin.readline().split())
measureNum = 0

for i in range(1, n+1):
    if(n % i == 0):
        measureNum += 1
        if(measureNum == k):
            print(i)
            break

if measureNum < k:
    print(-1)

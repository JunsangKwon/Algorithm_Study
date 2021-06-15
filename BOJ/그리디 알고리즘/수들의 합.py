import sys

n = int(sys.stdin.readline().strip())
sumOfn = 0

if(n == 1):
    print(1)
    exit()

for k in range(1, n+1):
    sumOfn += k
    if(sumOfn > n):
        print(k-1)
        break

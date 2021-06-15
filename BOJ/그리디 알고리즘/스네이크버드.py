import sys

n, l = map(int, sys.stdin.readline().strip().split())

fruits = list(map(int, sys.stdin.readline().strip().split()))

fruits.sort()

if(fruits[0] > l):
    print(l)
    exit()

for i in range(n):
    if(fruits[i] <= l):
        l += 1
    else:
        break

print(l)

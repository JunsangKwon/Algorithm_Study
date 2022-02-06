from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
count = 0

for i in range(n):
    array_sum = array[i]
    if array_sum == m:
        count += 1
        continue
    for j in range(i+1, n):
        array_sum += array[j]
        if(array_sum == m):
            count += 1
            break

print(count)

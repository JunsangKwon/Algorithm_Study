n = int(input())
arr = list(map(int, input().split()))
notprime = 0

for i in arr:
    if(i == 1):
        notprime += 1
        continue
    for j in range(2, i):
        if(i % j == 0):
            notprime += 1
            break

print(n - notprime)

m = int(input())
n = int(input())
primeNums = []

for i in range(m, n+1):
    if(i == 1):
        continue

    isPrime = True
    for j in range(2, i):
        if(i % j == 0):
            isPrime = False
            break
    if(isPrime):
        primeNums.append(i)

if(len(primeNums) == 0):
    print(-1)
else:
    print(sum(primeNums))
    print(min(primeNums))

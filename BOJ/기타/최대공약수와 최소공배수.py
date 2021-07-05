n, m = map(int, input().split())
divisorN = []
divisorM = []
commonDivisor = []
maxDivisor = 0
minMultiple = 0


for i in range(1, min(n, m)+1):
    if(n % i == 0):
        divisorN.append(i)
    if(m % i == 0):
        divisorM.append(i)

for i in divisorN:
    if(i in divisorM):
        commonDivisor.append(i)

maxDivisor = max(commonDivisor)  # 최대 공약수
minMultiple = maxDivisor * (n//maxDivisor) * (m//maxDivisor)

print(maxDivisor)
print(minMultiple)

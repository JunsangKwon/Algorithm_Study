from sys import stdin, stdout
from itertools import combinations

t = int(stdin.readline())
answer = []

for _ in range(t):
    n, *arr = map(int, stdin.readline().split())
    combinationList = list(combinations(arr, 2))
    gcd = 0
    candidateValue = 0
    for i in range(len(combinationList)):
        for j in range(min(combinationList[i]), 0, -1):
            if(combinationList[i][0] % j == 0 and combinationList[i][1] % j == 0):
                candidateValue = j
                break
        gcd += candidateValue
    answer.append(gcd)

for i in answer:
    print(i)

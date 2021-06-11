import sys

e, s, m = map(int, sys.stdin.readline().strip().split())
i = 1
j = 1
k = 1
year = 1

while(True):
    if(i == e and j == s and k == m):
        print(year)
        break
    i += 1
    j += 1
    k += 1
    if(i > 15):
        i = 1
    if(j > 28):
        j = 1
    if(k > 19):
        k = 1
    year += 1

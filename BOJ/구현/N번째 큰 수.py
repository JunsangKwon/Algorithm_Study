t = int(input())
arrs = []
answers = []

for i in range(t):
    tmparr = list(map(int, input().split()))
    arrs.append(tmparr)

for arr in arrs:
    arr.sort()
    answers.append(arr[-3])

for a in answers:
    print(a)

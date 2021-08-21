from sys import stdin

olim = list(map(int, stdin.readline().split()))
startlink = list(map(int, stdin.readline().split()))
olim_score = 0
startlink_score = 0
is_reversal = False


for i in range(9):
    olim_score += olim[i]
    if(olim_score > startlink_score):
        is_reversal = True
        break
    startlink_score += startlink[i]

if is_reversal:
    print("YES")
else:
    print("NO")

n = int(input())
score = []
answer = 0

for _ in range(n):
    tmp = int(input())
    score.append(tmp)

for i in range(n-1, 0, -1):
    if(score[i] <= score[i-1]):
        while(score[i] <= score[i-1]):
            score[i-1] -= 1
            answer += 1

print(answer)

from sys import stdin

questions = []
total_score = 0
final_quesion = []

for i in range(8):
    questions.append([int(stdin.readline()), i+1])

questions.sort(key=lambda x: (-x[0], x[1]))

for i in range(5):
    total_score += questions[i][0]
    final_quesion.append(questions[i][1])

final_quesion.sort()

print(total_score)
for num in final_quesion:
    print(num, end=' ')

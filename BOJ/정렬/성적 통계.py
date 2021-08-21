from sys import stdin

k = int(stdin.readline())
scores_list = []
gap_list = []
answer = []

for i in range(k):
    n, *scores = map(int, stdin.readline().split())
    scores.sort(reverse=True)
    answer.append([scores[0], scores[-1]])
    scores_list.append(scores)

for i in range(len(scores_list)):
    for j in range(len(scores_list[i])-1):
        gap_list.append(scores_list[i][j] - scores_list[i][j+1])
    answer[i].append(max(gap_list))
    gap_list.clear()


for i in range(k):
    print("Class %d" % (i+1))
    print("Max %d, Min %d, Largest gap %d" %
          (answer[i][0], answer[i][1], answer[i][2]))

answers = []

for _ in range(int(input())):
    coor_dic = {}
    count_dic = {}
    w = input()
    k = int(input())
    alpha = []
    candidate_word = []

    for i in range(len(w)):
        if w[i] in coor_dic:
            count_dic[w[i]] += 1
            coor_dic[w[i]].append(i)
            if count_dic[w[i]] == k:
                alpha.append(w[i])
        else:
            count_dic[w[i]] = 1
            coor_dic[w[i]] = [i]
            if k == 1:
                alpha.append(w[i])

    for i in range(len(alpha)):
        for j in range(count_dic[alpha[i]] - (k-1)):
            candidate_word.append(
                [alpha[i], coor_dic[alpha[i]][j + (k-1)] - coor_dic[alpha[i]][j] + 1])

    if len(alpha) == 0:
        answers.append([-1])
        continue

    candidate_word.sort(key=lambda x: x[1])
    answers.append([candidate_word[0][1], candidate_word[-1][1]])

for i in range(len(answers)):
    for j in range(len(answers[i])):
        print(answers[i][j], end=" ")
    print()

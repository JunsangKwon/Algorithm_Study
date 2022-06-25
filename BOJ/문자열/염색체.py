t = int(input())
strings = ['A', 'B', 'C', 'D', 'E', 'F']
word_list = []
determine = []

for i in range(t):
    word_list.append(input())

for i in range(len(word_list)):
    continue_flag = False
    dna = word_list[i]
    # 1단계
    if dna[0] not in strings:
        determine.append("Good")
        continue

    # 2, 3, 4 단계
    indexs = []
    for j in range(len(dna)):
        if dna[j] == 'A':
            indexs.append(j)
            break

    for j in range(len(dna)):
        if dna[j] == 'F':
            indexs.append(j)
            break

    for j in range(len(dna)):
        if dna[j] == 'C':
            indexs.append(j)
            break

    if len(indexs) != 3:
        determine.append("Good")
        continue
    else:
        if indexs[0] < indexs[1] and indexs[1] < indexs[2]:
            count = 0
            for j in range(indexs[2] + 1, len(dna)):
                if dna[j] not in strings:
                    determine.append("Good")
                    continue_flag = True
                    break
                else:
                    count += 1

            if continue_flag:
                continue
            if count > 1:
                determine.append("Good")
            else:
                determine.append("Infected!")
        else:
            determine.append("Good")

for i in range(len(determine)):
    print(determine[i])

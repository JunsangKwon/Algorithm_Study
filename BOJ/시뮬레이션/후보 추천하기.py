n = int(input())
m = int(input())
recommend = list(map(int, input().split()))
pics = {}
candidates = []

for i in range(len(recommend)):
    if recommend[i] in candidates:
        pics[recommend[i]][0] += 1
    else:
        if len(candidates) == n:
            delete_list = []
            for j in range(len(candidates)):
                tmp = []
                tmp.append(candidates[j])
                tmp.append(pics[candidates[j]][0])
                tmp.append(pics[candidates[j]][1])
                delete_list.append(tmp)
            delete_list.sort(key=lambda x: (x[1], x[2]))
            candidates.remove(delete_list[0][0])
            del pics[delete_list[0][0]]

        pics[recommend[i]] = [1, i]
        candidates.append(recommend[i])

candidates.sort()

for c in candidates:
    print(c, end=" ")

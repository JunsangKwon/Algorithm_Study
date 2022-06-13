words = []

t = int(input())
for _ in range(t):
    word = list(input())
    n = len(word)
    flag1 = False
    sort_index = 0
    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
            if word[i] > word[j]:
                tmp = word[j]
                word[j] = word[i]
                word[i] = tmp
                sort_index = j
                flag1 = True
                break
            elif word[i] == word[j] and i - j != 1:
                break
        if flag1:
            break

    if flag1:
        left_word = word[:sort_index+1]
        right_word = word[sort_index+1:]
        right_word.sort()
        new_word = left_word + right_word
        words.append(''.join(new_word))
    else:
        words.append(''.join(word))

for w in words:
    print(w)

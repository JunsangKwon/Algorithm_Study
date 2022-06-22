def solution(n, words):
    answer = []
    previous_words = []
    start_word = ''
    defeat_index = -1

    for i in range(len(words)):
        if i == 0:
            previous_words.append(words[i])
            start_word = words[i][-1]
        else:
            if words[i] in previous_words:
                defeat_index = i
                break
            else:
                if start_word == words[i][0]:
                    previous_words.append(words[i])
                    start_word = words[i][-1]
                else:
                    defeat_index = i
                    break

    if defeat_index == -1:
        answer = [0, 0]
    else:
        answer.append((defeat_index % n) + 1)
        answer.append((defeat_index // n) + 1)

    return answer

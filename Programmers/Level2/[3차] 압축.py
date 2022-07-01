from collections import deque


def solution(msg):
    answer = []
    word_dic = {}
    for i in range(ord('A'), ord('Z') + 1):
        word_dic[chr(i)] = i - 64

    index = 0
    dictionary_index = 27
    q = deque(list(msg))
    while q and index < len(msg):
        tmp_word = msg[index]
        q.popleft()
        while len(q) > 0:
            word = q.popleft()
            if tmp_word + word in word_dic:
                tmp_word = tmp_word + word
                index += 1
            else:
                q.appendleft(word)
                break

        if len(q) == 0:
            answer.append(word_dic[tmp_word])
            break
        else:
            answer.append(word_dic[tmp_word])
            word_dic[tmp_word + q[0]] = dictionary_index
            dictionary_index += 1
            index += 1

    return answer

def solution(s):
    answers = []
    s_length = len(s)
    for i in range(1, (s_length // 2) + 1):
        count = 1
        index = 0
        answer = ''
        while (index + 2 * i) <= s_length:
            if s[index: index + i] == s[index + i: index + 2 * i]:
                count += 1
                index += i
                if (index + 2 * i) > s_length:
                    answer += str(count) + s[index: index + i]
                    answer += s[index + i:]
            else:
                if count == 1:
                    answer += s[index: index + i]
                else:
                    answer += str(count) + s[index: index + i]
                count = 1
                index += i
                if (index + 2 * i) > s_length:
                    answer += s[index:]

        answers.append(len(answer))

    if s_length == 1:
        return 1
    return min(answers)

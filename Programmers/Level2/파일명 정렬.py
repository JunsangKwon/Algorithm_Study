def solution(files):
    answer = []
    files_detail = []

    for i in range(len(files)):
        head = ''
        number = ''
        tail = ''
        finish_flag = False
        for j in range(len(files[i])):
            if files[i][j].isalpha() or files[i][j] == ' ' or files[i][j] == '.' or files[i][j] == '-':
                if finish_flag:
                    tail = files[i][j:]
                    break
                head += files[i][j]
            else:
                finish_flag = True
                number += files[i][j]
        files_detail.append([head, number, tail, i])

    files_detail.sort(key=lambda x: (x[0].lower(), int(x[1]), x[3]))

    for i in range(len(files_detail)):
        file = ''
        for j in range(len(files_detail[i])-1):
            file += str(files_detail[i][j])
        answer.append(file)

    return answer

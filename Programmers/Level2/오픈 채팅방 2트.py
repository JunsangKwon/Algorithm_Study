def solution(record):
    answer = []
    nickname_dic = {}

    for i in range(len(record)):
        record_list = record[i].split(' ')
        if record_list[0] == 'Enter' or record_list[0] == 'Change':
            nickname_dic[record_list[1]] = record_list[2]

    for i in range(len(record)):
        record_list = record[i].split(' ')
        if record_list[0] == 'Enter':
            msg = nickname_dic[record_list[1]] + '님이 들어왔습니다.'
            answer.append(msg)
        elif record_list[0] == 'Leave':
            msg = nickname_dic[record_list[1]] + '님이 나갔습니다.'
            answer.append(msg)
    return answer

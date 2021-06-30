def solution(record):
    answer = []
    orders = []
    ids = []
    Dic = {}
    for r in record:
        words = list(map(str, r.split()))
        orders.append(words[0])
        ids.append(words[1])
        if(words[0] == 'Enter' or words[0] == 'Change'):
            Dic[words[1]] = words[2]

    for i in range(len(record)):
        if(orders[i] == 'Enter'):
            answer.append("%s님이 들어왔습니다." % Dic[ids[i]])
            continue
        elif(orders[i] == 'Leave'):
            answer.append("%s님이 나갔습니다." % Dic[ids[i]])
            continue
        else:
            continue

    return answer

def solution(id_list, report, k):
    report_dic = {}
    mail_dic = {}
    mail_count_dic = {}
    answer = []
    report = list(set(report))
    black_list = []

    for i in range(len(id_list)):
        report_dic[id_list[i]] = 0
        mail_dic[id_list[i]] = []
        mail_count_dic[id_list[i]] = 0

    for i in range(len(report)):
        info = report[i].split(" ")
        report_dic[info[1]] += 1
        mail_dic[info[1]].append(info[0])
        if report_dic[info[1]] >= k:
            black_list.append(info[1])

    black_list = list(set(black_list))

    for black in black_list:
        for i in range(len(mail_dic[black])):
            mail_count_dic[mail_dic[black][i]] += 1

    for i in range(len(id_list)):
        answer.append(mail_count_dic[id_list[i]])

    return answer

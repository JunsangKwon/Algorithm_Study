import math


def solution(fees, records):
    car_list = []
    time_list = []
    fee_list = []
    record_dic = {}
    standard_time = fees[0]
    standard_fee = fees[1]
    plus_time = fees[2]
    plus_fee = fees[3]

    for i in range(len(records)):
        record = records[i].split()
        if record[1] not in car_list:
            record_dic[record[1]] = []
            car_list.append(record[1])
            record_dic[record[1]].append(record[0])
        else:
            record_dic[record[1]].append(record[0])

    for car in car_list:
        if len(record_dic[car]) % 2 == 1:
            record_dic[car].append('23:59')

    car_list.sort()

    for i in range(len(car_list)):
        num = len(record_dic[car_list[i]])
        num = num // 2
        time = 0
        for j in range(num):
            in_hour = int(record_dic[car_list[i]][2 * j][:2])
            in_min = int(record_dic[car_list[i]][2 * j][3:])
            in_time = in_hour * 60 + in_min

            out_hour = int(record_dic[car_list[i]][2 * j + 1][:2])
            out_min = int(record_dic[car_list[i]][2 * j + 1][3:])
            out_time = out_hour * 60 + out_min

            time += out_time - in_time
        time_list.append(time)

    for i in range(len(time_list)):
        time = time_list[i]
        if time <= standard_time:
            fee_list.append(standard_fee)
        else:
            left_time = time - standard_time
            left_fee = math.ceil(left_time / plus_time) * plus_fee
            fee_list.append(standard_fee + left_fee)

    return fee_list

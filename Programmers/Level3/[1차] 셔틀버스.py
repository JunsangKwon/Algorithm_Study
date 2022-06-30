def solution(n, t, m, timetable):
    answer = ''
    bus_list = []
    possible_times = []
    bus_time = '09:00'
    timetable.sort()
    visited = [False] * len(timetable)

    for i in range(n):
        if i == 0:
            bus_list.append(bus_time)
            continue
        bus_hour = int(bus_time[:2])
        bus_min = int(bus_time[3:])
        if bus_min + t < 60:
            if bus_min + t < 10:
                bus_time = bus_time[:2] + ':0' + str(bus_min + t)
            else:
                bus_time = bus_time[:2] + ':' + str(bus_min + t)
        else:
            bus_hour_str = ''
            if bus_hour + 1 < 10:
                bus_hour_str = '0' + str(bus_hour + 1)
            else:
                bus_hour_str = str(bus_hour + 1)
                if bus_hour + 1 >= 24:
                    continue

            if bus_min + t - 60 < 10:
                bus_time = bus_hour_str + ':0' + str(bus_min + t - 60)
            else:
                bus_time = bus_hour_str + ':' + str(bus_min + t - 60)

        bus_list.append(bus_time)

    for i in range(len(bus_list)):
        bus_hour = int(bus_list[i][:2])
        bus_min = int(bus_list[i][3:])
        con_time = ''
        capacity = m
        is_full = False
        for j in range(len(timetable)):
            crew_hour = int(timetable[j][:2])
            crew_min = int(timetable[j][3:])
            if (crew_hour < bus_hour or (crew_hour == bus_hour and crew_min <= bus_min)) and not visited[j]:
                capacity -= 1
                visited[j] = True
                if capacity == 0:
                    if crew_min - 1 < 0:
                        if crew_hour - 1 < 10:
                            con_time = '0' + str(crew_hour - 1) + ':' + '59'
                        else:
                            con_time = str(crew_hour - 1) + ':' + '59'
                    else:
                        if crew_min - 1 < 10:
                            con_time = timetable[j][:2] + \
                                ':0' + str(crew_min - 1)
                        else:
                            con_time = timetable[j][:2] + \
                                ':' + str(crew_min - 1)
                    is_full = True
                    break

        if not is_full:
            possible_times.append(bus_list[i])
        else:
            possible_times.append(con_time)

    possible_times.sort(reverse=True)

    return possible_times[0]

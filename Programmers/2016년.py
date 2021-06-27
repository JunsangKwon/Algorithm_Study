def solution(a, b):
    answer = ''
    totaldays = 0
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    for i in range(a-1):
        totaldays += days[i]

    totaldays += b-1
    answer = week[totaldays % 7]

    return answer

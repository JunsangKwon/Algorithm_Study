def solution(phone_number):
    stars = ''
    backNum = ''
    for i in range(len(phone_number)-4):
        stars += '*'
    for i in range(-4, 0):
        backNum += phone_number[i]

    return stars + backNum

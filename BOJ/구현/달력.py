n = int(input())
calendar = [0]*367
dates = []
dimention = 0
max_value = -1
start_index = 0
flag = False

for i in range(n):
    date = list(map(int, input().split()))
    dates.append(date)

dates.sort(key=lambda x: (x[0], -x[1]))

for i in range(n):
    for j in range(dates[i][0], dates[i][1]+1):
        calendar[j] += 1

for i in range(367):
    if not flag and calendar[i] != 0:
        flag = True
        start_index = i
        max_value = calendar[i]
    elif flag and calendar[i] != 0:
        if max_value < calendar[i]:
            max_value = calendar[i]
    elif flag and calendar[i] == 0:
        width = i - start_index
        dimention += width * max_value
        max_value = -1
        flag = False

print(dimention)

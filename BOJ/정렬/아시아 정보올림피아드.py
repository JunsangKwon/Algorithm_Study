from sys import stdin

input = stdin.readline

records = []
n = int(input())
winners = []

for i in range(n):
    record = list(map(int, input().split()))
    records.append(record)

records.sort(key=lambda x: (-x[2], x[0], x[1]))
winners.append([records[0][0], records[0][1]])
winners.append([records[1][0], records[1][1]])

if(records[0][0] == records[1][0]):
    country = records[0][0]
    for i in range(2, len(records)):
        if(records[i][0] == country):
            continue
        else:
            winners.append([records[i][0], records[i][1]])
            break
else:
    winners.append([records[2][0], records[2][1]])

for i in range(len(winners)):
    print("%d %d" % (winners[i][0], winners[i][1]))

print(records)

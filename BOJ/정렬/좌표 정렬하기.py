from sys import stdin

coordinates = []
n = int(stdin.readline())
for i in range(n):
    coordinate = list(map(int, stdin.readline().split()))
    coordinates.append(coordinate)

coordinates.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print("%d %d" % (coordinates[i][0], coordinates[i][1]))

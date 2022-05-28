n, m = map(int, input().split())
bulbs = list(map(int, input().split()))

for i in range(m):
    operator, x, y = map(int, input().split())
    if operator == 1:
        bulbs[x-1] = y
    elif operator == 2:
        for j in range(x-1, y):
            if bulbs[j] == 0:
                bulbs[j] = 1
            else:
                bulbs[j] = 0
    elif operator == 3:
        for j in range(x-1, y):
            bulbs[j] = 0
    else:
        for j in range(x-1, y):
            bulbs[j] = 1

for b in bulbs:
    print(b, end=" ")

a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end="")
    if(i != b-1):
        print()

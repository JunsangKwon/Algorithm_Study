from sys import stdin

input = stdin.readline

cow_list = []
n = int(input())
for i in range(n):
    cow_info = list(map(int, input().split()))
    cow_list.append(cow_info)

cow_list.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    if(i == n-1):
        print(sum(cow_list[i]))
        break
    else:
        if(sum(cow_list[i]) > cow_list[i+1][0]):
            cow_list[i+1][0] = sum(cow_list[i])
        else:
            continue

print(cow_list)

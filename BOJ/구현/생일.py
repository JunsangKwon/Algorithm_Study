from sys import stdin

n = int(stdin.readline())
info_str_list = []

for i in range(n):
    info = list(input().split())
    info_str_list.append(info)

for i in range(n):
    info_str_list[i][1] = int(info_str_list[i][1])
    info_str_list[i][2] = int(info_str_list[i][2])
    info_str_list[i][3] = int(info_str_list[i][3])

info_str_list.sort(key=lambda x: (-x[3], -x[2], -x[1]))

print(info_str_list[0][0])
print(info_str_list[-1][0])

import sys

bingopan = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]


nums = []
for _ in range(5):
    nums += list(map(int, input().split()))

for i in range(25):
    breakpoint = True

    for j in range(5):
        for k in range(5):
            if(bingopan[j][k] == nums[i]):
                visited[j][k] = True
                breakpoint = False
                break
        if(breakpoint == False):
            break

    if i >= 10:
        # 가로줄 빙고, # 세로줄 빙고
        bingo = 0

        for l in range(5):
            if(visited[l][0] and visited[l][1] and visited[l][2]
                    and visited[l][3] and visited[l][4]):
                bingo += 1

            if(visited[0][l] and visited[1][l] and visited[2][l]
                    and visited[3][l] and visited[4][l]):
                bingo += 1

        # 대각선 빙고
        if(visited[0][0] and visited[1][1] and visited[2][2]
                and visited[3][3] and visited[4][4]):
            bingo += 1

        if(visited[0][4] and visited[1][3] and visited[2][2]
                and visited[3][1] and visited[4][0]):
            bingo += 1

        if(bingo >= 3):
            print(i+1)
            break

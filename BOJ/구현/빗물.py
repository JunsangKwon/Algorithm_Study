h, w = map(int, input().split())
world = [[0] * w for _ in range(h)]
block_height = list(map(int, input().split()))
visited = [[False] * w for _ in range(h)]
global left_count
left_count = 0
global right_count
right_count = 0
rain = 0


def find_block(wi, wj, move):
    flag = False
    left = 0
    right = 0
    global left_count
    global right_count

    if move == -1:
        while wj > 0:
            wj += move
            left += 1
            visited[wi][wj] = True
            if world[wi][wj] == 1:
                flag = True
                left -= 1
                left_count = left
                return True
        if not flag:
            return False
    else:
        while wj < w-1:
            wj += move
            right += 1
            visited[wi][wj] = True
            if world[wi][wj] == 1:
                flag = True
                right -= 1
                right_count = right
                return True
        if not flag:
            return False


for i in range(w):
    height = block_height[i]
    for j in range(h-1, h - height - 1, -1):
        world[j][i] = 1

for i in range(h):
    for j in range(w):
        if world[i][j] == 0 and not visited[i][j]:
            if find_block(i, j, -1) and find_block(i, j, 1):
                rain += left_count + right_count + 1
                left_count = 0
                right_count = 0

print(rain)

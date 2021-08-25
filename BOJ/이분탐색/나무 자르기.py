from sys import stdin, stdout

input = stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0

while(start <= end):
    tree_total_height = 0
    height = (start + end) // 2
    tree_total_height = sum(i-height if i > height else 0 for i in trees)

    if tree_total_height < m:
        end = height - 1
    else:
        start = height + 1
        result = height

print(result)

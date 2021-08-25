from sys import stdin, stdout

input = stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
sum_budget = int(input())

start = 0
end = max(budgets)
result = 0

while(start <= end):
    total = 0
    max_line = (start + end) // 2
    total = sum(max_line if b > max_line else b for b in budgets)

    if total > sum_budget:
        end = max_line - 1
    else:
        start = max_line + 1
        result = max_line

print(result)

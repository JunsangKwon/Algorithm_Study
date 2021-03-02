n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)
count = 0
answer = 0
for i in range(m):
    if(count == k):
        answer += array[1]
        count = 0
    else:
        answer += array[0]
        count += 1
print(answer)

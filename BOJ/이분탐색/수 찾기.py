
def search(arr, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
answer = []

n_list.sort()

for i in range(m):
    answer.append(search(n_list, m_list[i], 0, m-1))

print(answer)

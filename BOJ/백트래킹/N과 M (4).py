n, m = map(int, input().split())
arr = [0] * 10
isused = [0] * 10


def go(k):
    if(k == m):
        for i in range(m):
            if(i == m-1):
                print(arr[i])
            else:
                print(arr[i], end=" ")
        return

    for i in range(1, n+1, 1):
        if(isused[i] < m):
            if(k >= 1 and arr[k-1] > i):
                continue
            arr[k] = i
            isused[i] += 1
            go(k+1)
            isused[i] -= 1


go(0)

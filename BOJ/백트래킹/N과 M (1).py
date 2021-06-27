n, m = map(int, input().split())
arr = [0] * 10
isused = [False] * 10


def go(k):
    if(k == m):
        for i in range(m):
            if(i == m-1):
                print(arr[i])
            else:
                print(arr[i], end=" ")
        return

    for i in range(1, n+1, 1):
        if(not isused[i]):
            arr[k] = i
            isused[i] = True
            go(k+1)
            isused[i] = False


go(0)

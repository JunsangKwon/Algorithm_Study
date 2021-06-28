n, m = map(int, input().split())
narr = list(map(int, input().split()))
narr.sort()
arr = [0] * n
isused = [False] * n


def go(k):
    if(k == m):
        for i in range(m):
            if(i == m-1):
                print(arr[i])
            else:
                print(arr[i], end=" ")
        return

    for i in range(len(narr)):
        if(not isused[i]):
            arr[k] = narr[i]
            isused[i] = True
            go(k+1)
            isused[i] = False


go(0)

n, m = map(int, input().split())
narr = list(map(int, input().split()))
narr.sort()
arr = [0] * n
isused = [0] * n


def go(k):
    if(k == m):
        for i in range(m):
            if(i == m-1):
                print(arr[i])
            else:
                print(arr[i], end=" ")
        return

    for i in range(len(narr)):
        if(isused[i] < m):
            arr[k] = narr[i]
            isused[i] += 1
            go(k+1)
            isused[i] -= 1


go(0)

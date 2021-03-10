n = int(input())
pslist = []
stack = []
flag = False

for i in range(n):
    ps = list(input())
    pslist.append(ps)

for i in range(n):
    for j in pslist[i]:
        if j == '(':
            stack.append(0)
        elif j == ')':
            if(len(stack) == 0):
                flag = True
                break
            stack.pop()

    if not flag and len(stack) == 0:
        print("YES")

    else:
        flag = False
        print("NO")
        stack.clear()

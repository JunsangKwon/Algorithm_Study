# sol1. '('의 빈도와 ')'의 빈도가 같으면 된다? -> )))(((는 VPS가 아님 (X)
# sol2. list를 stack으로 사용하여 '(' 가 들어오면 push, ')'가 들어오면 pop을 한다.
# -> stack의 크기가 0보다 작아지려하면 "NO"출력, 끝난 후 stack의 크기가 0보다 커도 "NO"출력
# -> 끝난 후 stack의 크기가 딱 0이라면 "YES" 출력

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
            stack.append(0)         # 임의의 값 0을 스택에 추가
        elif j == ')':
            if(len(stack) == 0):    # 스택의 크기가 0보다 작아짐 -> NO
                flag = True
                break
            stack.pop()

    if not flag and len(stack) == 0:  # 스택의 크기가 0보다 작아진적 없고, stack의 길이가 0 이다. -> YES
        print("YES")

    else:
        flag = False                # stack의 길이가 0 이상이다. -> NO
        print("NO")
        stack.clear()

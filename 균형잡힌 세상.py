# Sol. 괄호 심화버전, stack1, 2, 3를 둔다. stack1 -> () 유지하는 조건, stack2 -> []유지하는 조건,
# stack3 -> ( 다음에 ] or [ 다음에 ) 가 오는걸 방지하는 조건

sentences = []
stack1 = []
stack2 = []
stack3 = []
flag1 = False
flag2 = False
flag3 = False

while True:                     # 입력받기, .이 들어오면 입력 멈춤
    sentence = input()
    if(sentence == "."):
        break
    sentences.append(sentence)

for i in range(len(sentences)):
    for j in sentences[i]:
        # ( 가 들어오면 stack1에는 임의의 값을 추가하고, stack3에는 자신을 추가한다.
        if(j == "("):
            stack1.append(0)
            stack3.append(j)
        # [ 가 들어오면 stack2에는 임의의 값을 추가하고, stack3에는 자신을 추가한다.
        elif(j == "["):
            stack2.append(0)
            stack3.append(j)
        # ) 가 들어오면 stack1을 확인하여 앞에 (가 있었는지를 확인하고 stack3를 확인하여 [ 가 제일 최근에 있었는지를 확인한다.
        elif j == ")":
            if(len(stack1) == 0 or len(stack3) == 0):
                flag1 = True
                break
            if(stack3[-1] == "["):
                flag3 = True
                break
            stack1.pop()
            stack3.pop()
        # ] 가 들어오면 stack2을 확인하여 앞에 [가 있었는지를 확인하고 stack3를 확인하여 (가 제일 최근에 있었는지를 확인한다.
        elif j == "]":
            if(len(stack2) == 0 or len(stack3) == 0):
                flag2 = True
                break
            if(stack3[-1] == "("):
                flag3 = True
                break
            stack2.pop()
            stack3.pop()
        continue

    # 모든 조건을 다 만족시켰다면 yes
    if not flag1 and not flag2 and not flag3 and len(stack1) == 0 and len(stack2) == 0:
        print("yes")

    # 조건을 만족시키지 못했다면 no
    else:
        flag1 = False
        flag2 = False
        flag3 = False
        stack1.clear()
        stack2.clear()
        stack3.clear()
        print("no")

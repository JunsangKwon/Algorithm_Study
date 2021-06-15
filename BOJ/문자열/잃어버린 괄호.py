expression = input()
exlist = list(expression)       # 문자열 중간의 문자를 수정하기 위해 str를 문자 list로 변환함
isMinus = False                 # sol. -가 나온 후엔 다음 -가 나오기 전까지의 +를 전부 -로 바꿔서 계산함
operlist = []                   # 연산자를 저장하는 배열

for i in range(len(exlist)):
    if(exlist[i] == '-'):
        isMinus = True          # - 가 나온 후엔 isMinus 값을 True로 바꾼다.
        operlist.append(exlist[i])
    if(exlist[i] == '+'):
        if(isMinus):            # - 가 앞에 나왔으면 -로 변환, 아니라면 +로 계산한다.
            exlist[i] = '-'
        operlist.append(exlist[i])

expression = ''.join(exlist)    # 문자 list를 다시 str 형태로 변환한다.
# str에서 기호를 빈칸으로 바꾼 후 빈칸을 기준으로 숫자를 뽑아낸다.
numlist = list(expression.replace('+', ' ').replace('-', ' ').split())

result = int(numlist[0])        # 문자로 저장되있기 때문에 int로 형 변환, 결과 값에 맨 처음 값을 세팅해준다.
for i in range(len(operlist)):
    if(operlist[i] == '+'):     # 기호 배열의 값이 + 면 더하고, -면 뺀다.
        result += int(numlist[i+1])
    else:
        result -= int(numlist[i+1])

print(result)

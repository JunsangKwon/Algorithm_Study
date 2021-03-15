# sol. 튜플을 사용해서 우선순위를 정해 정렬한다.
n = int(input())
tuplelist = []

for i in range(n):
    tmplist = []
    tmpword = input()
    tmplen = len(tmpword)
    tmplist.append(tmplen)              # 문자 길이를 튜플의 첫 번째 요소에 저장
    tmplist.append(tmpword)             # 문자를 튜플의 두 번째 요소에 저장
    tuplelist.append(tuple(tmplist))    # 리스트를 튜플로 변환

# 첫 요소를 기준으로 정렬 하고, 같으면 두번째 요소를 기준으로 정렬해라
tuplelist.sort(key=lambda x: (x[0], x[1]))
tmp = " "  # 중복 제거를 위한 임의의 값 지정

for (_, word) in tuplelist:
    if tmp == word:         # 바로 전의 값과 중복이면 출력하지 않고 중복이지 않으면 출력해라
        continue
    print(word)
    tmp = word              # 출력 한 값을 저장 해둠

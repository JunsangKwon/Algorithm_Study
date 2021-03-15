# sol. 연속 중복을 하나로 처리 후 (어차피 상관없음), 다음에 같은 문자가 오면 그룹문자가 아닌거로 처리

n = int(input())
words = []
already = []
count = 0
flag = False
for i in range(n):                  # 배열에 단어 저장
    word = input()
    words.append(word)

for i in range(n):
    tmp = '-'                       # 중복 체크하는 변수
    for j in range(len(words[i])):
        if(tmp == words[i][j]):     # 중복은 continue로 무시
            continue
        else:
            already.append(words[i][j])     # 중복이 아니면 already라는 배열에 문자를 추가한다
            tmp = words[i][j]               # 중복체크 변수에 방금 추가된 값을 저장

    for k in already:                       # already에 저장된 문자의 수가 배열 내에 몇개있는지 확인한다.
        cnt = already.count(k)
        if cnt != 1:                        # 배열내에 문자가 1개가 아니라면 그룹단어가 아닐 것
            flag = True

    if not flag:                            # 배열내에 문자가 1개라면 그룹단어로 인정하여 count에 +1 해줌
        count += 1

    flag = False
    already.clear()                         # already 배열을 초기화 후 다시 반복문 돌림

print(count)

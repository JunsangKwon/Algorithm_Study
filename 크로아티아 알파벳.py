# sol. 그냥 노가다로 함
alpha = input()
count = 0

for i in range(len(alpha)-1):
    if(alpha[i] == 'c'):            # c=, c- 처리
        if(alpha[i+1] == '=' or alpha[i+1] == '-'):
            continue
    if(alpha[i] == 'd'):
        if(alpha[i+1] == '-'):      # d- 처리
            continue
        if(alpha[i+1] == 'z'):
            if(i+2 == len(alpha)):  # dz로 단어가 끝나는 경우 처리 (반례)
                count += 1
            continue
    if(alpha[i] == 'z'):            # dz=, z= 처리
        if(i-1 >= 0 and alpha[i-1] == 'd'):
            if(alpha[i+1] == '='):
                continue
            else:
                count += 2
                continue
        if(alpha[i+1] == '='):
            continue
    if(alpha[i] == 's'):            # s= 처리
        if(alpha[i+1] == '='):
            continue
    if(alpha[i] == 'l' or alpha[i] == 'n'):  # lj, nj 처리
        if(alpha[i+1] == 'j'):
            continue

    count += 1          # 그 외의 다른 알파벳은 +1 해줌

print(count+1)          # 마지막 알파벳은 확인하지않고 +1 처리 해줌

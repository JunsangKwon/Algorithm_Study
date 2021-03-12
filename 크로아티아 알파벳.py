alpha = input()
count = 0

for i in range(len(alpha)-1):
    if(alpha[i] == 'c'):
        if(alpha[i+1] == '=' or alpha[i+1] == '-'):
            continue
    if(alpha[i] == 'd'):
        if(alpha[i+1] == '-'):
            continue
        if(alpha[i+1] == 'z'):
            if(i+2 == len(alpha)):  # dzdz 처리
                count += 1
            continue
    if(alpha[i] == 'z'):
        if(i-1 >= 0 and alpha[i-1] == 'd'):
            if(alpha[i+1] == '='):
                continue
            else:
                count += 2
                continue
        if(alpha[i+1] == '='):
            continue
    if(alpha[i] == 's'):
        if(alpha[i+1] == '='):
            continue
    if(alpha[i] == 'l' or alpha[i] == 'n'):
        if(alpha[i+1] == 'j'):
            continue

    count += 1

print(count+1)

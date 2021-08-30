from sys import stdin

input = stdin.readline

card_list = []
answer = []

P = [0]*13
K = [0]*13
H = [0]*13
T = [0]*13

count_p = 0
count_k = 0
count_h = 0
count_t = 0

s = input()

for i in range(0, len(s)-2, 3):
    card_list.append(s[i] + s[i+1] + s[i+2])

if(len(set(card_list)) != len(card_list)):
    print("GRESKA")
else:
    for i in range(len(card_list)):
        if(card_list[i][0] == 'P'):
            P[int(card_list[i][1] + card_list[i][2])-1] = 1
        elif(card_list[i][0] == 'K'):
            K[int(card_list[i][1] + card_list[i][2])-1] = 1
        elif(card_list[i][0] == 'H'):
            H[int(card_list[i][1] + card_list[i][2])-1] = 1
        elif(card_list[i][0] == 'T'):
            T[int(card_list[i][1] + card_list[i][2])-1] = 1

    for i in range(13):
        if(P[i] == 0):
            count_p += 1
        if(K[i] == 0):
            count_k += 1
        if(H[i] == 0):
            count_h += 1
        if(T[i] == 0):
            count_t += 1

    print("%d %d %d %d" % (count_p, count_k, count_h, count_t))

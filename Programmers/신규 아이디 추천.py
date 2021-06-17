def solution(new_id):
    trigger = False
    idlist = ['A']*len(new_id)

    # 1단계
    new_id = new_id.lower()

    # 2단계 (문제 있음)
    for i in range(len(new_id)):
        idlist[i] = new_id[i]

    new_id = ''

    for i in range(len(idlist)):
        if(ord(idlist[i]) >= 97 and ord(idlist[i]) <= 122):
            continue
        if(ord(idlist[i]) >= 48 and ord(idlist[i]) <= 57):
            continue
        if(idlist[i] == '-' or idlist[i] == '_' or idlist[i] == '.'):
            continue
        idlist[i] = 'A'

    idlist.replace('A', '')

    # 3단계
    for s in idlist:
        if(trigger):
            if(s == '.'):
                idlist.remove(s)
            trigger = False
        if(s == '.'):
            trigger = True

    for i in range(len(idlist)):
        new_id += idlist[i]

    print(new_id)

    # 4단계
    if(new_id != ""):
        if(new_id[0] == '.'):
            new_id = new_id.replace(new_id[0], "")
        elif(new_id[-1] == '.'):
            new_id = new_id.replace(new_id[-1], "")

    # 5단계
    if(new_id == ""):
        new_id = "a"

    # 6단계
    if(len(new_id) >= 16):
        new_id = new_id[0:15]
        if(new_id[-1] == '.'):
            new_id = new_id.replace(new_id[-1], "")

    # 7단계
    if(len(new_id) <= 2):
        if(len(new_id) == 1):
            new_id = new_id * 3
        else:
            new_id += new_id[-1]

    return new_id

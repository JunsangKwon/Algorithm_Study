passwords = []
determine = []
mo = ['a', 'e', 'i', 'o', 'u']
ja = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
      'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

while True:
    valid_flag = False
    password = input()
    if password == 'end':
        break
    passwords.append('<' + password)

    # 1단계
    for i in range(5):
        if mo[i] in password:
            valid_flag = True
            break

    if not valid_flag:
        determine.append("> is not acceptable.")
        continue

    # 2단계
    ja_count = 0
    mo_count = 0
    for i in range(len(password)):
        if password[i] in mo:
            ja_count = 0
            mo_count += 1
            if mo_count == 3:
                valid_flag = False
                break
        else:
            mo_count = 0
            ja_count += 1
            if ja_count == 3:
                valid_flag = False
                break

    if not valid_flag:
        determine.append("> is not acceptable.")
        continue

    # 3단계
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            if password[i] == 'e' or password[i] == 'o':
                continue
            else:
                valid_flag = False

    if not valid_flag:
        determine.append("> is not acceptable.")
        continue
    else:
        determine.append("> is acceptable.")

for i in range(len(passwords)):
    print(passwords[i] + determine[i])

n = int(input())
keys = []
results = []

for i in range(n):
    finish_flag = False
    option = input()

    if option[0].lower() not in keys:
        keys.append(option[0].lower())
        option_list = list(option)
        option_list.insert(0, '[')
        option_list.insert(2, ']')
        option = ''.join(option_list)
        results.append(option)
        finish_flag = True
    else:
        for i in range(len(option)):
            if option[i] == ' ' and option[i+1].lower() not in keys:
                keys.append(option[i+1].lower())
                option_list = list(option)
                option_list.insert(i+1, '[')
                option_list.insert(i+3, ']')
                option = ''.join(option_list)
                results.append(option)
                finish_flag = True
                break

        if not finish_flag:
            for i in range(1, len(option)):
                if option[i] != ' ' and option[i].lower() not in keys:
                    keys.append(option[i].lower())
                    option_list = list(option)
                    option_list.insert(i, '[')
                    option_list.insert(i+2, ']')
                    option = ''.join(option_list)
                    results.append(option)
                    finish_flag = True
                    break

    if not finish_flag:
        results.append(option)

for r in results:
    print(r)

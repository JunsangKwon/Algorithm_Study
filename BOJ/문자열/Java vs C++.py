var = input()
isError = False
determine = 0

if '_' in var:
    determine = 1

if determine == 1:
    word_list = var.split('_')
    java_value = ''
    for i in range(len(word_list)):
        if word_list[i] == '' and not word_list[i].islower():
            isError = True
            break
        else:
            if i == 0:
                java_value += word_list[i]
            else:
                word_list[i] = word_list[i][0].upper() + word_list[i][1:]
                java_value += word_list[i]

    if not isError:
        print(java_value)
    else:
        print("Error!")
else:
    c_word_list = []
    var = list(var)
    tmp_word = ''
    for i in range(len(var)):
        if i == 0 and var[i].isupper():
            isError = True
            break

        if var[i].isupper():
            c_word_list.append(tmp_word)
            tmp_word = var[i].lower()
        else:
            tmp_word += var[i]

    c_word_list.append(tmp_word)

    if not isError:
        print('_'.join(c_word_list))
    else:
        print("Error!")

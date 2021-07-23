def words(s, index, length):
    numword = ''
    for j in range(index, index+length):
        numword += s[j]
    return numword


def solution(s):
    answer = ''
    num_list = []
    num_dictionary = {'zero': '0', 'one': '1', 'two': '2', 'three': '3',
                      'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                      'eight': '8', 'nine': '9'}

    i = 0
    while(i < len(s)):
        if(ord(s[i]) > 47 and ord(s[i]) < 58):
            num_list.append(s[i])
            i += 1
        elif(s[i] == 'o'):
            value = words(s, i, 3)
            num_list.append(num_dictionary[value])
            i += 3
        elif(s[i] == 'z' or s[i] == 'f' or s[i] == 'n'):
            value = words(s, i, 4)
            num_list.append(num_dictionary[value])
            i += 4
        elif(s[i] == 'e'):
            value = words(s, i, 5)
            num_list.append(num_dictionary[value])
            i += 5
        elif(s[i] == 's'):
            if(s[i+1] == 'i'):
                value = words(s, i, 3)
                num_list.append(num_dictionary[value])
                i += 3
            else:
                value = words(s, i, 5)
                num_list.append(num_dictionary[value])
                i += 5
        elif(s[i] == 't'):
            if(s[i+1] == 'w'):
                value = words(s, i, 3)
                num_list.append(num_dictionary[value])
                i += 3
            else:
                value = words(s, i, 5)
                num_list.append(num_dictionary[value])
                i += 5
        else:
            continue

    for num in num_list:
        answer += num

    return int(answer)

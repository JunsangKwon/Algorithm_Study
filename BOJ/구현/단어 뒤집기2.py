sentence = input()
new_sentence = ''
tag_flag = False
tmp_sentence = ''
is_final_alpha = False

for i in range(len(sentence)):
    if tag_flag:
        new_sentence += sentence[i]
        if sentence[i] == '>':
            tag_flag = False
    elif sentence[i] == '<':
        tag_flag = True
        if tmp_sentence != '':
            new_sentence += tmp_sentence[::-1]
            tmp_sentence = ''
        new_sentence += sentence[i]
    elif sentence[i] == ' ':
        new_sentence += tmp_sentence[::-1]
        new_sentence += ' '
        tmp_sentence = ''
    else:
        tmp_sentence += sentence[i]
        if i == len(sentence) - 1:
            is_final_alpha = True

if is_final_alpha:
    new_sentence += tmp_sentence[::-1]


print(new_sentence)

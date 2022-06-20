def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    tmp_id = ''
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.' or new_id[i].isdigit():
            tmp_id += new_id[i]

    new_id = tmp_id

    # 3단계
    stack = []
    for i in range(len(new_id)):
        stack.append(new_id[i])
        if i == len(new_id) - 1:
            break
        elif stack[-1] == new_id[i+1] == '.':
            stack.pop()

    new_id = ''.join(stack)

    # 4단계
    if len(new_id) >= 2:
        if new_id[0] == '.':
            new_id = new_id[1:]

        if new_id[-1] == '.':
            new_id = new_id[:-1]
    elif len(new_id) == 1:
        if new_id[0] == '.':
            new_id = ''

    # 5단계
    if len(new_id) == 0:
        new_id += 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

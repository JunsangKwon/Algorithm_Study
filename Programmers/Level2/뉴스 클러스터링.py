def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = []
    str2_set = []
    intersection = []
    union = []
    previous_word_i = []
    previous_word_u = []
    intersection_count = 0
    union_count = 0
    
    for i in range(len(str1)-1):
        if 97 <= ord(str1[i]) and ord(str1[i]) <= 122 and 97 <= ord(str1[i+1]) and ord(str1[i+1]) <= 122:
            str1_set.append(str1[i] + str1[i+1])
    
    for i in range(len(str2)-1):
        if 97 <= ord(str2[i]) and ord(str2[i]) <= 122 and 97 <= ord(str2[i+1]) and ord(str2[i+1]) <= 122:
            str2_set.append(str2[i] + str2[i+1])

        
    if len(str1_set) == 0 and len(str2_set) == 0:
        return 65536
    elif len(str1_set) > len(str2_set):
        str1_set, str2_set = str2_set, str1_set

    
    for i in range(len(str1_set)):
        if str1_set[i] in str2_set:
            if str1_set[i] in previous_word_i:
                continue
            str1_count = str1_set.count(str1_set[i])
            str2_count = str2_set.count(str1_set[i])
            intersection.append([str1_set[i], min(str1_count, str2_count)])
            previous_word_i.append(str1_set[i])

    
    for i in range(len(str1_set)):
        if str1_set[i] in str2_set:
            if str1_set[i] in previous_word_u:
                continue
            str1_count = str1_set.count(str1_set[i])
            str2_count = str2_set.count(str1_set[i])
            union.append([str1_set[i], max(str1_count, str2_count)])
            previous_word_u.append(str1_set[i])
        else:
            union.append([str1_set[i], 1])
    
    for i in range(len(str2_set)):
        if str2_set[i] not in previous_word_u:
            union.append([str2_set[i], 1])
    
    for i in range(len(intersection)):
        intersection_count += intersection[i][1]
        
    for i in range(len(union)):
        union_count += union[i][1]

    answer = int(intersection_count / union_count * 65536)
    
    
    return answer
a, b = input().split()

a_length = len(a)
b_length = len(b)
diff_list = []
diff = 0

if a_length > b_length:
    a_length, b_length = b_length, a_length

if a_length < b_length:
    for i in range(b_length - a_length + 1):
        diff = 0
        for j in range(i, i + a_length):
            if a[j - i] != b[j]:
                diff += 1
        diff_list.append(diff)
    print(min(diff_list))
else:
    for i in range(a_length):
        if a[i] != b[i]:
            diff += 1
    print(diff)

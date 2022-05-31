n, k = map(int, input().split())
course = list(map(int, input().split()))
reverse_course = course[::-1]
course += reverse_course
total = 0
ans = 0

for i in range(len(course)):
    total += course[i]
    print(total)
    if total < k:
        continue
    elif total == k:
        if i > n-1:
            ans = 2 * n - i
        elif i == n-1:
            ans = n
        else:
            ans = i + 2
        break

    else:
        if i > n-1:
            ans = 2 * n - i
        else:
            ans = i + 1
        break


print(ans)

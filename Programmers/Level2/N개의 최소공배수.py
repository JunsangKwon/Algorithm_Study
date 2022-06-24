def solution(arr):
    arr.sort()
    new_arr = arr

    while len(new_arr) != 1:
        f_divisors = []
        s_divisors = []
        max_divisor = -1

        for i in range(1, new_arr[0] + 1):
            if(new_arr[0] % i == 0):
                f_divisors.append(i)

        for i in range(1, new_arr[1] + 1):
            if(new_arr[1] % i == 0):
                s_divisors.append(i)

        for i in range(len(f_divisors)-1, -1, -1):
            if f_divisors[i] in s_divisors:
                max_divisor = f_divisors[i]
                break

        least_mul = (new_arr[0] // max_divisor) * \
            (new_arr[1] // max_divisor) * max_divisor
        new_arr.pop(0)
        new_arr[0] = least_mul

    return new_arr[0]

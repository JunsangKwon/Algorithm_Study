def solution(numbers):
    all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    no_numbers = []

    for n in all_numbers:
        if n not in numbers:
            no_numbers.append(n)

    answer = sum(no_numbers)
    return answer
